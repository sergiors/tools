import re

"""
               Head=1
               |
               | __________Tail=[2,3,4,5]
               ||
              [1,2,3,4,5]
[1,2,3,4]=Init________||
                       |
                       |
                  5=Last
"""
def palindrome(data: str):
    data = re.sub(r'\W+', '', data).lower()

    eq = data[0] == data[-1]
    mid = data[1:-1]

    if mid:
        return eq & palindrome(mid)

    return eq


if __name__ == '__main__':
    assert(True == palindrome('Rotor'))
    assert(True == palindrome('Racecar'))
    assert(True == palindrome('Arara'))
    assert(True == palindrome('my gym'))
    assert(True == palindrome('Red rum, sir, is murder'))
    assert(False == palindrome('Lincoln'))

