#!/usr/bin/env PYTHONIOENCODING=utf-8 python
# encoding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

# built-in
import os
import subprocess
import sys

FS_ENCODING = sys.getfilesystemencoding()


def apply_linter(cmd, files, **kwargs):
    if not files:
        return
    print('Running %s' % cmd[0])
    return subprocess.check_output(cmd + files, stderr=subprocess.STDOUT, **kwargs).decode(FS_ENCODING)


def filter_files(files, extension):
    return [f for f in files if f.endswith(extension)]


def lint_files(changed_files):
    changed_extensions = {ext for root, ext in map(os.path.splitext, changed_files)}

    if '.py' in changed_extensions:
        py_files = filter_files(changed_files, '.py')
        apply_linter(['isort'], py_files)
        apply_linter(['yapf', '-i'], py_files)
        apply_linter(['flake8'], py_files)


if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))

    changed_files = subprocess.check_output('git diff --cached --name-only --diff-filter=ACM'.split())
    changed_files = changed_files.decode(FS_ENCODING)
    changed_files = [f.strip() for f in changed_files.splitlines()]

    try:
        lint_files(changed_files)
    except subprocess.CalledProcessError as exc:
        print('Quality check failed:', file=sys.stderr)
        print(' '.join(exc.cmd), file=sys.stderr)
        if exc.output:
            output = exc.output.decode(FS_ENCODING)
            print('\t', '\n\t'.join(output.splitlines()), sep='', file=sys.stderr)
        sys.exit(1)
