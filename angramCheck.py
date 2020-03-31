# given two strings, check if they're angrams

def andgram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    if len(s1) != len(s2):
        return False
    else:
        for s in s1:
            if s not in s2:
                return False
        return True
       

