# Given a list of lists (lols) that will need to be color coded later based on a trend determined by the following rules:
# 
# 1. If the first number of a row is higher than the second number of the previous row, append the string `up` to the row
# 2. If the first number of a row is lower than the second number of the previous row, append the string `down` to the row
# 3. Otherwise, append `same` to the row.
# 
# Obviously, you cannot apply these rules to the first row (there is no preceding row), so append an empty string for the first row.
# 
# Basically think of this as a list of Open/Close values, and we want to assign the values `same`, `up`, or `down` based on
# how a row's Open value compares to the Close of the previous row.
# 
# For example, given the following list:

data = [
    [10, 20],
    [20, 30],
    [35, 50],
    [45, 60]
]

# Then after your code finishes running, your `data` should look like this:
"""
[
    [10, 20, ''],
    [20, 30, 'same'],
    [35, 50, 'up'],
    [45, 60, 'down']
]
"""

# SOLUTION:

cont = [] # create empty list container
for row_idx, row in enumerate(data):
  cont_el = [None] # create list container to be `cont` element
  if row_idx == 0:
    for col_idx, col in enumerate(row):
      cont_el.append(col)
    cont.append(cont_el)
    data[row_idx].append('')
  else:
    for col_idx, col in enumerate(row):
      cont_el[0] = cont[-1][-1]
      cont_el.append(col)
    cont.append(cont_el)
    if cont[-1][1] > cont[-1][0]:
      data[row_idx].append('up')
    elif cont[-1][1] < cont[-1][0]:
      data[row_idx].append('down')
    else:
      data[row_idx].append('same')

#print(cont)
print(data)





