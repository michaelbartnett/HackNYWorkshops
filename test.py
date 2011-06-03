from scipy.weave import converters
#source: http://fperez.org/talks/0204_python-c.pdf

if __name__ == '__main__'
  code = """ C CODE GOES HERE """
  err = weave.inline(code, [VARIABLES, GO, HERE], type_converters=converters.blitz, compiler='gcc')
  return err
