#Think of at least five places in the world you’d like to visit.Store the locations in a list. Make sure the list is not in alphabetical order.
locations = ['helio park', 'city center', 'burj al arab', 'dubai mall', 'rawabi supermarket']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)