def greatest(*nos):
   result = nos[0]
   for e in nos:
        if e > result:
           result = e
   return result
print(greatest(18,400,50))
