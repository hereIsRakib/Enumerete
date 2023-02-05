# Checking index of 50
search_range = int(input('How large is the range? ex:100 \n'))
search_index = int(input('The desired number to find index: \n'))
index = 0
for i, num in enumerate(range(1, search_range)):
    print(i, num)  # this will show the index and number
    if num == search_index:
        index = i

print('The index of 50 is: ', index)
