def add(*args):
  total=0
  for i in args:
    if isinstance(i,(int,float)):
      total+=i
    else:
      print(f"skipping this {i} as it is non numeric")
  return total

print(add(4,29,10,"er",4.2))
