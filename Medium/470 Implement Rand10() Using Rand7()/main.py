# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        x = rand7()
        while(x == 4):
            x = rand7()
        #x < 4:
        if x == 1:
            x = rand7()
            while(x <= 2):
                x = rand7()
            if x <= 5:
                return 1
            else:
                return 2
        if x == 2:
            x = rand7()
            while(x <= 2):
                x = rand7()
            if x <= 3:
                return 2
            if x <= 6:
                return 3
            else:
                return 4
        if x == 3:
            x = rand7()
            while(x <= 2):
                x = rand7()
            if x <= 4:
                return 4
            else:
                return 5
        #x > 4:
        if x == 5:
            x = rand7()
            while(x <= 2):
                x = rand7()
            if x <= 5:
                return 6
            else:
                return 7
        if x == 6:
            x = rand7()
            while(x <= 2):
                x = rand7()
            if x <= 3:
                return 7
            if x <= 6:
                return 8
            else:
                return 9
        if x == 7:
            x = rand7()
            while(x <= 2):
                x = rand7()
            if x <= 4:
                return 9
            else:
                return 10

            
