from pyscript import document

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    for item in problems:
        split_item = item.split()
        first = split_item[0]
        operator = split_item[1]
        second = split_item[2]

        if not (operator == '+' or operator == '-'):
            return "Error: Operator must be '+' or '-'."
        if not (first.isdigit() and second.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'


    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    for index, item in enumerate(problems):
        first = item.split()[0]
        second = item.split()[2]
        operator = item.split()[1]

        #first line
        first_line += ' ' * (max(len(first), len(second)) + 2 - len(first))
        first_line += first
        if len(problems) > index + 1:
            first_line += 4 * ' '

        #second line
        second_line += operator + ' ' 

        if len(first) > len(second):
            second_line += ' ' * (max(len(first), len(second)) - min(len(first), len(second)))

        second_line += second;

        if len(problems) > index + 1:
            second_line += 4 * ' '

        #third line
        third_line += '-' * (max(len(first), len(second))+2)
        if len(problems) > index + 1:
            third_line += 4* ' '

        #fourth line
        op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
        result = op[operator](int(first),int(second))

        if index == 0:
            fourth_line = ' ' * (len(third_line)  - 4 - len(str(result)))
            fourth_line += str(result)
        else:
            if item[index+1] != None:
                fourth_line += 4 * ' '
            res_len = len(str(result))
            third_line_len = max(len(first), len(second)) + 2

            if res_len > third_line_len:
                fourth_line += ' ' * (res_len - third_line_len) + str(result)
            else:
                fourth_line += (third_line_len - res_len) * ' ' + str(result)

    res = first_line + '\n' + second_line + '\n' + third_line
    if show_answers:
        res += '\n' + fourth_line
    return res
