class Stack():
    my_Steck = []
    def isEmpty(self):
        if len(self.my_Steck) == 0:
            return True
        else:
            return False

    def push(self, adds_element):
        self.my_Steck.append(adds_element)
        return " "

    def pop(self):
        last_element = self.my_Steck[-1]
        self.my_Steck.pop()
        return last_element

    def peek(self):
        return self.my_Steck[-1]

    def size(self):
        return len(self.my_Steck)


def check_bracket(bracket_string):
    stack = Stack
    if bracket_string[0] == "}" or bracket_string[0] == ")" or bracket_string[0] == "]":
        print("Несбалансированно")
        raise StopIteration
    for bracket in bracket_string:
        if bracket == "(" or bracket == "[" or bracket == "{":
            stack.push(stack, bracket)

        elif bracket == ")" and stack.peek(stack) == "(":
            stack.pop(stack)

        elif bracket == "]" and stack.peek(stack) == "[":
            stack.pop(stack)

        elif bracket == "}" and stack.peek(stack) == "{":
            stack.pop(stack)

        else:
            print('fw')

    if stack.size(stack) == 0:
        print("Сбалансированно")
    else:
        print("Несбалансированно")

check_bracket("{[()]}")





