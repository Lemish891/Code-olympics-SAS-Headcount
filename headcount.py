def neighbours(i, j, rows, columns, array):
    if i < 0 or i >= rows or j < 0 or j >= columns or array[i][j] == 0:
        return 0
    array[i][j] = 0
    size = 1
    size += neighbours(i+1, j, rows, columns, array)
    size += neighbours(i-1, j, rows, columns, array)
    size += neighbours(i, j+1, rows, columns, array)
    size += neighbours(i, j-1, rows, columns, array)
    return size

def count_groups_and_size(array):
    rows, columns = len(array), len(array[0])
    groups = []
    people = 0

    num_groups = 0
    for i in range(rows):
        for j in range(columns):
            if array[i][j] == 1:
                size = neighbours(i, j, rows, columns, array)
                people += size
                groups.append(size)
                num_groups += 1

    groups.sort(reverse=True)
    print(str(num_groups) + " teams of " + str(groups) + " totaling " + str(people))


array = [[1,1,0,0,0,0,1,1],

 [1,1,0,1,1,0,1,1],

 [0,0,0,1,1,0,0,0],

 [1,1,0,1,1,0,1,1],

 [1,1,0,0,0,0,1,1]]
count_groups_and_size(array)