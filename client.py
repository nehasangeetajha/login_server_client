import socket

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.connect((host, port))

    def createacc():
        def createusername():
            username = input('Username: ')
            return username
            
        def createpassword():
            password = input('Password (must be atleast 8 characters) : ')
            if len(password)<8:
                print('Password too short')
                return createpassword()
            else:
                return password
            
        username = createusername()
        password = createpassword()
        s.sendall(response.encode())
        s.sendall(username.encode())
        s.sendall(password.encode())
        print(s.recv(1024).decode())
       

        print('Your Account has been created, please login using same username and password')








    response  = input('If you want to\nLogin, press 1\nCreate New Account, press 2\nDelete Existing Account, press 3\n: ')
    if(response==1):
        sendLoginInformation(s)
    elif(response==2):
        createacc()
    #elif(response==3):
        #delacc()
    else:
        print("invalid input")
	
def sendLoginInformation(s):
	
    print("Enter 1 if u want to login, 2 to create account")
    check = input("Choice: ")
    if check == 1 : 
        print("Welcome please Log in.")
        username = input("Username: ")
        password = input("Password: ")
        s.sendall(check)
        s.sendall(username.encode())
        s.sendall(password.encode())
        print(s.recv(1024).decode())
        
        print("Would you like to logout?")
        response = input("Yes or No >> ")
        s.sendall(response.encode())
        print(s.recv(1024).decode())
    
    elif check == 2 :
        username = input("Create a username:")
        password = input("Create a password:")
        s.sendall(response)
        s.sendall(username.encode())
        s.sendall(password.encode())
        print(s.recv(1024).decode())
        
    s.close()

main()