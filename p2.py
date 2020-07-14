class LargeNumber(object):
    def addTwoNumbers(self, n1, n2):
        if len(n1) > len(n2):
            lc = len(n1) - len(n2)
            n2 = '{}{}'.format(r'0' * lc, n2)
        elif len(n1) < len(n2):
            lc = len(n2) - len(n1)
            n1 = '{}{}'.format(r'0' * lc, n1)
        result = [0] * (len(n1)+1)
        list1 = list(n1[::-1])
        list2 = list(n2[::-1])
        for i, v in enumerate(list1):
            v_add = int(list2[i]) + int(v) + result[i]
            if v_add >= 10:
                m, va = divmod(v_add, 10)
                result[i] = va
                result[i + 1] = m
            else:
                result[i] = v_add
        if result[i+1] == 0:
            result = result[:-1]
        print(''.join('%s' % vi for vi in result[::-1]))
        return True


