import requests

username=input("Enter the username : ")


link="https://www.codechef.com/users/"+username
code=requests.get(link)
source_code=code.text


tmp=source_code.index('Problems Solved')

source_code=source_code[tmp:]

tmp=source_code.index('(')

ans=source_code[tmp+1:]

tmp=ans.index("</h5>")

ans=ans[:tmp-1]

ans=int(ans)

print("Number of problems solved by %s is %d"%(username,ans))