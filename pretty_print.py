# function to read file into a list
def read_text(txt_file):
    text = []
    with open(txt_file) as file:
        for line in file:
            line = line.split()
            text += line
    return text


# function to generate one line cost matrix
def one_line_cost(text, m):
    cost_matrix = [[0 for i in range(len(text))] for j in range(len(text))]
    for i in range(len(text)):
        for j in range(i, len(text)):
            cost = m - j + i - sum([len(x) for x in text[i:(j+1)]])
            if cost < 0:
                cost = m**3
            cost_matrix[i][j] = cost**3
    return cost_matrix


def pretty_print(txt_file, m):
    # read the text file
    text = read_text(txt_file)
    n = len(text)

    # generate one line costs
    cost_matrix = one_line_cost(text, m)

    # initial matrix
    p = [0 for i in range(n)]
    breaks = [0 for i in range(n)]

    # loop through updated optimal penalties
    for j in range(1, n):
        p[j] = m**3 * n
        for i in range(1, j):
            if (p[i - 1] != m**3 * n) and (cost_matrix[i][j] != m**3 * n):
                new_pj = p[i - 1] + cost_matrix[i][j]
                if new_pj < p[j]:
                    p[j] = new_pj
                    breaks[j] = i - 1

    # print total penalty
    print(p[n - 1])

    # use breaks matrix to find where new lines should go
    current = breaks[n - 1]
    new_lines = []
    while current != 0:
        new_lines.append(current)
        current = breaks[current]
    new_lines.reverse()

    # print the paragraph
    j = 0
    for i, word in enumerate(text):
        if (j < len(new_lines)) and (i == new_lines[j]):
            print(word, end = "\n")
            j += 1
        elif i == n - 1:
            print(word)
        else:
            print(word, end = " ")


pretty_print("buffy.txt", 72)
