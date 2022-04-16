def lcs(s1,s2):
    if (len(s1) < len(s2)):
        tmp = s1
        s1 = s2
        s2 = tmp
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for i in range(n2+1)] for j in range(2)]
    ans = 0

    for i in range(1,n1 + 1):
        for j in range(1,n2 + 1):
            if(s1[i - 1] == s2[j - 1]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                if(dp[i % 2][j] > ans):
                    ans = dp[i % 2][j]
            else:
                dp[i % 2][j] = 0

    return ans

