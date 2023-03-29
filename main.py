balanced_dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}

balanced_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
unbalanced_list = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack(list):

    def is_empty(self):
        return len(self) == 0

    def push(self, el):
        self.append(el)

    def pop(self):
        if not self.is_empty():
            items = self[-1]
            self.__delitem__(-1)
            return items

    def peek(self):
        if not self.is_empty():
            return self[-1]

    def size(self):
        return len(self)


def check(sequence):
    stack = Stack()
    for item in sequence:
        if item in balanced_dict:
            stack.push(item)
        elif item == balanced_dict.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.is_empty()


if __name__ == '__main__':
    for seq in balanced_list + unbalanced_list:
        print(f'{seq}{check(seq)}')
