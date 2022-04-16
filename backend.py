from lcs import lcs
from sort import Sort

def load_movies():
    mov = {}
    fil = open("movies.txt")
    for line in fil:
        r = line.split(",")
        for i in range(len(r)):
            r[i] = r[i].strip()
        mov[r[0]] = {"img":r[1], "com":int(r[2]) , "act":int(r[3])}
    return mov

def search(s,toSort):
    movies = load_movies()
    lst = []
    for x in movies.keys():
        n = lcs(x,s)
        if n > 3:
            lst.append((x,n))
    def comp(a1,a2):
        if a1[1] < a2[1]:
            return 1
        elif a1[1] > a2[1]:
            return -1
        else:
            return 0
    if toSort == "True":
        Sort(lst,comp)
    ast = lst
    if len(lst)>5:
        ast = lst[0:6]
    rst = []
    idx=0
    for x in ast:
        rst.append([idx,x[0],movies[x[0]]["img"]])
        idx += 1
    return rst



def search_recom(s,com,act):
    movies = load_movies()
    lst = []
    for x in movies.keys():
        n = lcs(x,s)
        if n > 1:
            lst.append((x,n,com*movies[x]["com"] + act*movies[x]["act"]))
    def comp(a1,a2):
        if a1[2] < a2[2]:
            return 1
        elif a1[2] > a2[2]:
            return -1
        elif a1[1] < a2[1]:
            return 1
        elif a1[1] > a2[1]:
            return -1
        else:
            return 0
    Sort(lst,comp)
    ast = lst
    if len(lst)>5:
        ast = lst[0:6]
    rst = []
    idx=0
    for x in ast:
        rst.append([idx,x[0],movies[x[0]]["img"]])
        idx += 1
    return rst
