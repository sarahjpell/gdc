import os


def findExpression(l):
    split = l.split('/t')
    expression = split[1]
    return expression

jup = 0
tp53 = 0
ctnnb1 = 0

jupList = []
tp53List = []
ctnnb1List = []

val = -1


for filename in os.listdir(os.getcwd()):
    open(filename, 'r')
    for line in filename:
        if "ENSG00000141510" in line:
            print("hi")
            tp53 += 1
            exp = findExpression(line)
            tp53List.append(exp)

        elif "ENSG00000168036" in line:
            ctnnb1 += 1
            exp = findExpression(line)
            ctnnb1List.append(exp)

        elif "ENSG00000173801" in line:
            jup += 1
            exp = findExpression(line)
            jupList.append(exp)


print("tp53")
print(tp53)
print(tp53List)

print("jup")
print(jup)
print(jupList)

print("ctnnb1")
print(ctnnb1)
print(ctnnb1List)