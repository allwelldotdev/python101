data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)

# Given the above tuple of lists:
#
# The program should:
# 1. Mutate the lists in `data` to add one more element indicating the distance between the two integer numbers
# (i.e. the absolute value for the difference).
# 2. Determine on which date this newly calculated value was the largest.
# 3. Be able to work for a `data` set containing any number of lists.

# SOLUTION:

# 1) adding abs distance between two integer numbers

for row_idx, row in enumerate(data):
  cont = [] # create empty list container
  for list_idx, list_item in enumerate(row):
    if list_idx == 1:
      cont.append(list_item)
    if list_idx == 2:
      cont.append(list_item)
  a, b = cont # unpack container values
  diff = abs(a - b)
  data[row_idx].append(diff) # append absolute difference value in list within `data` tuple

print(f'1) {data}')

# 2) on which date is calculated value the largest ?

cont = [] # create empty list container
for row_idx, row in enumerate(data):
  for list_idx, list_item in enumerate(row):
    if list_idx > 2:
      cont.append(list_item)
# find largest number
largest = cont[0]
for num in cont:
  if num > largest:
    largest = num
print(f'2.1) {largest}')
# which date has largest number ?
for row_idx, row in enumerate(data):
  if data[row_idx][-1] == largest:
    for list_idx, list_item in enumerate(row):
      if list_idx == 0:
        print(f'2.2) data[{row_idx}][{list_idx}] - {list_item} is date with largest absolute distance')


