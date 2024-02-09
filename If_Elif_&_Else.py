#username = "admin"
#check = 'admin'

#if username==check and 1==1:
#if username==check and 1==2:
#    print('Access Granted!')
#elif 1==1:
#    print('middle condition true!')
#elif 4==4:
#    print('tird condition!')
#else:
#    print("All above condition, were not true!")    

username = "john"
permission = True
 
if username == "admin" and permission:
     print("full Access")
elif username == 'admin' and permission==False:
    print("Admin access only, no full permission")
else:
    print("No access")