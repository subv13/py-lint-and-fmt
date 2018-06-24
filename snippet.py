from __future__ import unicode_literals, absolute_import
import os
import json
import sys

SOME_CONST =  123123


def url(reg, view, name):
    json.dumps({'kek': 'lol'})
    pass

class SomeViewWithLoooooooooooongName(object):
    def as_view(self):
        pass

urlpatterns = [
    url('orders/blalalalallalaalalalaalallal/<id>/bjljsdf', SomeViewWithLoooooooooooongName.as_view(), name='orders-blaaaaaalallalal')
]

class SomeClass(object):
    def __init__(self, kek=2, lol=3):
        self.kek = kek
        self.lol = lol

    def some_long_long_long_named_function_with_many_many_args(self, arg1, arg2, arg3, arg4, arg5, arg6):
        return ', '.join([arg1, arg2, arg3, arg4, arg5, arg6, self.kek, self.lol])

    def some_function_that_return_complex_structure(self):
        l = []
        for i in xrange(10):
            for j in xrange(2):
                l.append({
                    'key1': '123123',
                    'key2': '123123',
                    'key3': '{} {} {} {} {} {} {} {} {} {}'.format(1, '123', '3456', '343434343', '3535353535', 6, 7, 8, 9, 10), 'key4': i + j,
                    'key5': self.some_long_long_long_named_function_with_many_many_args('123123', '12312312312', '123123123', '123123', 2, 3)
                }) # yapf: disable

A_GLOBAL_DICT = {'asdf': 'asdfffffffffffffffffffffffffffffffffffffffff', 'dfdfs': 'asdfffffffffffffffffffffffffffffffffff'}

if __name__ == '__main__':
    some_instance = SomeClass()

    print some_instance.some_function_that_return_complex_structure()

    alist = []

    alist.append(
        {
            'key': 'value',
            'key2': 'value',
        }
    )

    list_compr = ['{} 1222222222222222222222222222222222222222222222222222222'.format(some_item) for some_item in xrange(1000)]
