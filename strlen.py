def count_vowels(s):
    c=0
    for i in s:
        if(i == 'a'or'e'or'i'or'o'or'u'):
            c+=1
    return c
def count_consonants(s):
    c=0
    for i in s:
        if(i!='a'or'e'or'i'or'o'or'u'):
            c+=1
    return c
def count_upper(s):
    c=0
    for i in s:
        if(i=="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            c+=1
    return c

if __name__  == "__main__":
    str = "programming"  
    res=count_vowels(str)
    print(res)
    res1=count_consonants(str)
    print(res1)
    res2 = count_upper(str)
    print(res2)