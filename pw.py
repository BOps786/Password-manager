import random as rd
import sys, pyperclip
def code(ch):
   l=list(ch)
   for i in range(len(l)) :
      l[i]=str(ord(l[i]))+chr(rd.randint(97,123))
   return ''.join(l)
def decode(ch):
   li=list(ch)
   i=0
   pre=0
   res=''
   while i<len(li) :
     if ord(li[i]) in range (97,123):
        res+=chr(int(''.join(li[pre:i])))
        pre=i
        li.pop(i)
     i+=1
     
   return res    

if len(sys.argv) < 2:
   print('Usage:if it exists, py pw.py [account] - copy account password.if not, you will be creating it , py pw.py [account] [password]  ')
   sys.exit()
elif len(sys.argv)==3:
   file=open(r"C:\Users\Pc\Desktop\Python_Projects\Passwords.txt",mode='a') 
   res="\n"+sys.argv[1]+' '+code(sys.argv[2])
   file.write(res)
   print('account added')
   file.close()
elif len(sys.argv)==2:
   file=open(r"C:\Users\Pc\Desktop\Python_Projects\Passwords.txt",mode='r') 
   acc = sys.argv[1] 
   lines=file.readlines()
   if acc in [((lines[i]).split(' '))[0] for i in range(len(lines))]:
      pyperclip.copy(decode([((lines[i]).split(' '))[1] for i in range(len(lines)) if ((lines[i]).split(' '))[0]==acc][0]))
      print('Password for ' +acc+ ' copied to clipboard.')
   else:
      print('There is no account named ' + acc)
   file.close()
else:
   print('Too many arguments provided. Usage: py pw.py [account] or py pw.py [account] [password]')
   sys.exit()







   


   




   
     

            

         