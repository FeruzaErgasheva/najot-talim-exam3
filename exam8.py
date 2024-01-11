fileProduct=open("products.txt","r")
fileK=open("k.txt","w")
fileA=open("a.txt","w")
words=fileProduct.read().split()
for word in words:
    a=word.lower().count("a")
    k=word.lower().count("k")
    if a!=0:
        fileA.write(word+" ")
    if k!=0:
        fileK.write(word+" ")

fileA.close()
fileK.close()
fileProduct.close()