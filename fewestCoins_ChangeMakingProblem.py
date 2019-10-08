coins=[1,5,10,25]
amount=21

def mincoin(coins,amount):
    max=amount+1
    dp=[max for x in range(max)]
    resultDic=dict()
    # for i in range(1, max):
    #     resultDic[i] = [0 for x in range(len(coins))]
    if len(dp)>1:
        dp[0]=0
        # print(dp)
        for i in range(1,max):
            for j in range(len(coins)):
                if coins[j]<=i:
                    if dp[i-coins[j]]+1<dp[i]:
                        dp[i]=dp[i-coins[j]]+1
                        resultDic[i] = [0 for x in range(len(coins))]
                        if type(resultDic.get(i-coins[j]))==list:
                            for key,item in enumerate(list(resultDic.get(i-coins[j]))):
                                resultDic[i][key]=item
                        resultDic[i][j]=resultDic[i][j]+1   #set current coin

        print(resultDic)
        if dp[amount]>amount:
            return False
        else:
            return resultDic[amount],dp[amount]

print(mincoin(coins,amount))
