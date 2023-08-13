class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        if not self.stack_list:
            return True
        return False

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)


def bracketing(example):

    open_closed = {'(': ')',
                   '[': ']',
                   '{': '}'}
    for char in example:
        if char in open_closed.keys():
            stack.push(char)
        elif char in open_closed.values():
            if stack.is_empty() or open_closed[stack.pop()] != char:
                return False
    return stack.is_empty()


if __name__ == '__main__':
    stack = Stack()
    expressions = ['(((([{}]))))',
                   '[([])((([[[]]])))]{()}',
                   '{{[()]}}',
                   '}{}',
                   '{{[(])]}}',
                   '[[{())}]']

    for example in expressions:
        print(bracketing(example))