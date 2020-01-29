import socket

Logins = [("python", "pythonrules"),
		  ("Alexa", "iloveit"),
		  ("Maria", "alone"),
		  ("taylor", "potterhead")
		  ]
		  
def initServer():
	s = socket.socket()
	host = socket.gethostname()
	port = 12345
	s.bind((host, port))
	s.listen(5)
	print('Server Listening...')
	print("Waiting for Connection")

	conn, addr = s.accept()
	print("Got connection from: ", addr)
    check = conn.recv()
	username = conn.recv(1024).decode()
	password = conn.recv(1024).decode()
    create = createacc(check,username,password) 
    login = validateLogin(username, password)
	conn.sendall(login.encode())

	response = conn.recv(1024).decode()
	Logout = logout(response)
	conn.sendall(Logout.encode())
	
	conn.close()

def createacc(check,username,password):
    if(check==1):
        return ""
    if(username,password) in Logins:
    return "Username already exists!!"
    Logins.update({username,password})

	
def validateLogin(check,username, password):
    if(check==2):
        return ""
	if(username, password) in Logins:
		return "Success, Welcome! " + username
	else:
		return "Fail, please try again."

def logout(response):
	if response == ("yes") or response == ("Yes") or response == ("YES"):
		return "Logout successful, See you next time!"
	elif response == ("no") or response == ("No") or response == ("NO"):
		return "Logout unsuccessful, Thanks for sticking around!"
	else:
		return "Command not valid, try Yes or No"
	
initServer()	