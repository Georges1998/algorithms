def balance_check(s):
    stack = []
    opening = set('({[')
    matches = set([
        ('[', ']'),
        ('(', ')'),
        ('{', '}'),
     ])

    if len(s) % 2 != 0:
        return False
    else:
        for i in s:
            if i in opening:
                stack.append(i)
            else:
               last_open = stack.pop() 
               if (last_open, i) not in matches:
                   return False
    return len(stack)==0

print(balance_check("({}{[])[(())"))