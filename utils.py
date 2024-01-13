s = "[({})]"
a = []
val = {
    "}":"{",
    ")":"(",
    "]":"["
}
for i in s :
    if i  not in val.keys() and i in val.values():
        a.append(i)
    elif i in val.keys():
        a.pop()

print(a)        


