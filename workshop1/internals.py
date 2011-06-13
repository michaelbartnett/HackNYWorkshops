Python Internals
class Name(bases):
    <body>
        -->
1. executes <body> "as if it was a function w/o arguments", create a dict d (w/ all the "locals" of that function)
2. find the class's metaclass M
3. Name = M(Name, bases, d)

def makeSandwich(wid='plenty'):
    class Philly(object):
        steak = 'you bet'
        cheese = 'swiss'
        if wid: onions = wid
        print locals()
makeSandwich()
makeSandwhich(None)

No such thing as delcarations, only statements.

import dis #disassembler
def f():
    class x(object):
        y = 23
dis.dis(f)

python has implicit None return
__ == dunder

Metaclass: type(M).__call__
    type.__call__ does 2 step construction:
    x = M.__new__(M, name, bases, d)
    if isinstance(x, M):
        M.__init__(x, name, bases, d)

Class Statement Limitations:
class body is executed BEFORE the metaclass M is known so M has no control.

class body execution returns a dict (so no order-relevance is possible)

Python 3: metaclass=M in class statement
M.__prepare__ can return any mapping
class decorators removes >50% of the use cases for custom metaclasses

x.foo -> getattr(x, 'foo')
x.foo = value -> setattr(x, 'foo', value)
x.foo += 1 -> gets then sets
__getattribute__ should not be overwritten

use inspect for introspection not dir, vars, __classes__, __bases__,
use inspect-stack for stack
debugging yes, testing maybe, NOT FOR PRODUCTION!

GC
enable, disable, isenabled, collect
get_debug, set_debug
get_threshold, set_threshold
get_objects, get_referrers, get_referents

Python's VM is stack oriented not register oriented.
POP_TOP, ROT_TWO... 0-operands... wicked fast!
operators: unary_not, binary_add, inplace_divide
slicing: binary_subscr, slice+0 == x[:], slice+1 == x[a:], slice+... 8 different operations

1 operand bytecodes:
    extended_arg (for 4 byte operands)
    load_: const, name, attr, global, fast, closure, deref
    store_:
    delete_:
    build_: tuple, list, map, slice
    flow control: jump_, setup_, call_, for_iter, raise_varargs
    setup_: loop, except, finally
    make_function, make_closure

I <3 python so freaking much.

USE DIS!
Byteplay (to see the real assembly)

