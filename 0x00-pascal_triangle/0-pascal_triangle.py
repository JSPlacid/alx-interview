def pascal_triangle(n):
     triangle = []
     for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
               current_row.append(1)
            else:
                outcome = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(outcome)

        triangle.append(current_row)

    return triangle


#n = 5
#pascal_triangle = pascal_triangle(n)
#for row in pascal_triangle:
#    print(row)
