def printLongestCommanSubstring(str1,str2,lstr1,lstr2):
    lengthLCS = 0
    r,c=0,0
    longestCommonArray = [[0 for i in range(0,lstr2+1)]for j in range(0,lstr1+1)]
    print(str1,str2,lstr1,lstr2)
    print(longestCommonArray)
    for i in range(lstr1+1):
        for j in range(lstr2+1):
            print("i: ",i," j: ",j)
            if i==0 or j==0:
                longestCommonArray[i][j]=0

            elif str1[i-1]==str2[j-1]:
                longestCommonArray[i][j]=longestCommonArray[i-1][j-1]+1
                if lengthLCS < longestCommonArray[i][j]:
                    lengthLCS = longestCommonArray[i][j]
                    r,c=i,j
                else:
                    longestCommonArray[i][j]=0
    if lengthLCS==0:
        print("noting is good")
        return ''
    resultStr = ['x' for i in range(lengthLCS)]

    while longestCommonArray[r][c]!=0:
        lengthLCS-=1
        resultStr[lengthLCS]=str1[r-1]
        r-=1
        c-=1
    final = ''.join(resultStr)
    print("resultStr",resultStr)
    return final



if __name__=="__main__":
    x= "sanjayisgood"
    y="sanjayd"
    l1= len(x)
    l2=len(y)
    print("finally answer:",printLongestCommanSubstring(x,y,l1,l2))

