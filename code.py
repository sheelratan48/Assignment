def reversestr(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = input()

print(" string,s : ", end="")
print(s)

print("The reversed of s is : ", end="")
print(reversestr(s))