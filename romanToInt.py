def romanToInt(s):
    valMap = {"M" : 1000,"D" : 500, "C" : 100,"L" : 50 ,"X" : 10, "V" : 5, "I" : 1}
    count = 0
    char = 0
    while char in range(0,len(s)):
        curVal = valMap.get(s[char])
        if(char + 1 != len(s)):
            nextVal = valMap.get(s[char+1])
        else:
            nextVal = 0
        if(curVal < nextVal):
            count+=(nextVal - curVal)
            char+=1
        else:
            count+=curVal
        char+=1
    return count


