def greatest(i,j,k):
    if (i>=j) and (i>=k):
        largest=i
    elif (j >=i) and (j >=k):
        largest=j
    else:
        largest=k
    return largest

i=10
j=20
k=30
print(greatest(i,j,k))