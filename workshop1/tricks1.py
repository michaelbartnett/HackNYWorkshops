# Guido Van Rossum 1991 aus NL
# interpreted, interactive, oo, multi-paradigm, exceptions, modules, dynamic typing, high level data types, classes, power, simple syntax

# switch two variables:
  a = 10
  b = 5
  a, b = b,a
# magic else 
for i in foo:
  if i == 0:
    break
else:
  print("i was never 0")
# operator overloading
# sets:
# { } makes a set or comprehension
a = set([1,2,3,4])
b = set([3,4,5,6])
a | b # union
a & b # intersection
a < b # subset
a - b # difference
a ^ b # symmetric difference
# strings:
'xyz'*3
'test' in 'is test in this string?'
# List Sclices
#
# List comprehensions
# Generators
# Decorators
# http://www.phyast.pitt.edu/~micheles/python/documentation.html
def print_args(function):
  def wrapper(*args, **kwargs):
    print 'Aguments:', args, kwargs
    return function(*args, **kwargs)
  return wrapper

@print_args
def write(text):
  print text

# Built-ins
lambda
zip(a,b)
map, reduce, filter # staples of functional programmer
# * and ** magic (splat)
* will unpack tuples
** will unpack dictionaries
# chaining comparison operators

# regex, regex debug
re.compile("""
 ^              # start of a line
 \[font         # the font tag
 (?:=(?P<size>  # optional [font=+size]
 [-+][0-9]{1,2} # size specification
 ))?
 \]             # end of tag
 (.*?)          # text between the tags
 \[/font\]      # end of the tag
 """, re.DEBUG|re.VERBOSE|re.DOTALL)

# yield
# multiplying by booleans
# round with negative precision
