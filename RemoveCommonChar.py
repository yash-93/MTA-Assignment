str1 = 'yash'
str2 = 'desp'


def compare(s, c):
    final = ''
    for ch in s:
        if ch not in c:
            final += ch
    return final


print(compare(str1, str2) + compare(str2, str1))
