# Union of Two or more sets

# A = {1, 2, 3}
# B = {3, 4, 5}
#
# print(A.union(B))

# Example No.5
# A = {'a', 'b', 'c'}
# B = {'b', 'c', 'd', 'e'}
# C = {'c', 'd', 'e', 'f', 'g'}
# # I have to find A U (BUC)
# BUC = B.union(C)
# AUBUC = A.union(BUC)
# print(AUBUC)

#...........................................................................

# Intersection of sets
# A = {1, 2, 3, 4}
# B = {3, 4, 5}
# print(A.intersection(B))

# # Example No.7
# A = {'a', 'b', 'c'}
# B = {'b', 'c', 'd', 'e'}
# C = {'c', 'd', 'e', 'f', 'g'}
# # Find: A intersection (BintercC)
# BintersecC = B.intersection(C)
# AintersecBintersecC = A.intersection(BintersecC)
# print(AintersecBintersecC)


#.....................................................................

# Guided Practice
# A = {1, 3, 5, 7, 9}
# B = {2, 3, 5, 7}
# # Find  AUB and A intersection B
# AUB = A.union(B)
# AintersecB = A.intersection(B)
# print(AUB)
# print(AintersecB)

#......................................................................
# Difference of two sets
# A = {2, 3, 4, 5, 6}
# B = {5, 6, 7, 8}
# AdiffB = A.difference(B)
# print(AdiffB)

# ..............................................................
# X = {'a', 'e', 'i', 'o', 'u'}
# Y = {'a', 'b', 'c', 'd', 'e'}
# # find Y-X
# YdiffX = Y.difference(X)
# print(YdiffX)

# ..................................................................
# Disjoint sets
# A = {3,4,5}
# B = {6,7,8}
# print(A.isdisjoint(B))


# A = {1,2,3,4,6,12}
# B = {3,6,9,12,18}
# AdiffB = A.difference(B)
# BdiffA = B.difference(A)
# print(f"A-B = {AdiffB}")
# print(f"B-A = {BdiffA}")
# if (AdiffB == BdiffA):
#     print("A-B and B-A are not equal")
# else:
#     print("A-B and B-A are equal")


def complement(arg):
    U = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    return U-arg

A = {2,4,6,8,10,12,14,16,18,20}
B = {1,3,5,7,9,12,15,17,19}
print("A complement = ", complement(A))
print("B complement = ", complement(B))
empty = set()
print("Empty set Complement = ", complement(empty))

AComplement = complement(A)
print("A Union A Complement = ", A.union(AComplement))

S = {1,2,3}
print("S Complement = ", complement(S))