plainText=input("ENTER THE PLAIN TEXt ").upper().replace('J',"I")
key=input("ENTER THE KEY ").upper().replace('J','I')
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
visited={i:0 for i in alphabets}
row={}
col={}
keyMat=[['a','a','a','a','a'] for i in range(5)]
i,j=0,0
for e in key:
    if(visited[e]==1):
        continue
    if(j<4):
        keyMat[i][j]=e
        row[e]=i
        col[e]=j
        j+=1
    else:
        keyMat[i][j]=e
        row[e]=i
        col[e]=j
        j=0
        i+=1
    visited[e]=1
for e in alphabets:
    if(e=='J'):continue
    if(visited[e]==1):
        continue
    if(j<4):
        keyMat[i][j]=e
        row[e]=i
        col[e]=j
        j+=1
    else:
        keyMat[i][j]=e
        row[e]=i
        col[e]=j
        j=0
        i+=1
    visited[e]=1
ans=""
for k in keyMat:print(k)
def playFair(c1,c2):
    if(row[c1]==row[c2]):
        t1,t2=col[c1],col[c2]
        return keyMat[row[c1]][(t1+1)%5]+keyMat[row[c2]][(t2+1)%5]
    elif(col[c1]==col[c2]):
        t1,t2=row[c1],row[c2]
        return keyMat[(t1+1)%5][col[c1]]+keyMat[(t2+1)%5][col[c2]]
    else:
        return keyMat[row[c1]][col[c2]]+keyMat[row[c2]][col[c1]]

i=0
while(i<len(plainText)):
    if(i==len(plainText)-1 or plainText[i]==plainText[i+1]):
        ans+=playFair(plainText[i],'X')
    else:
        ans+=playFair(plainText[i],plainText[i+1])
        i+=1
    i+=1
print(ans)


