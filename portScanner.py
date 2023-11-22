import socket

print("Starting the script....")
scanIP = input("Enter the IP to scan for ports : ")
portStart = int(input("Starting port to scan for "))
portEnd = int(input ("Ending port to scan "))

try:
	for i in range(portStart,portEnd):
		socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socketObj.settimeout(1)
		client = (scanIP, i)
		response = socketObj.connect_ex(client)
		if response == 0:
			print("Successful : "+ str(i))
		socketObj.close()	
except socket.error as e:
	print("Error : " + e)
print("Finished ....")

	


