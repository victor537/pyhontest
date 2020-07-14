class TwoStack(object):
    def __init__(self):
        self.array = []
        self.stackl = 0
        self.stackr = 0

    def l_push(self, data):
        self.array.insert(0, data)
        self.stackl += 1
        return True

    def l_pop(self):
        if self.stackl == 0:
            print('Stack a is empty')
            return False
        else:
            self.array.pop(0)
            self.stackl -= 1
            return True

    def r_push(self, data):
        self.array.append(data)
        self.stackr += 1
        return True

    def r_pop(self):
        if self.stackr == 0:
            print('Stack b is empty')
            return False
        else:
            self.array.pop()
            self.stackr -= 1
            return True
