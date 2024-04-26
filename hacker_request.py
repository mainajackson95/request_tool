import requests

url = input("Enter url: ")

r = requests.post(url)
#print(r.status_code)
#print(r.header)

cookies = r.cookies

data = {
	"command": "exist",
	"paths" : "anything.txt",
	"c2f": cookies['currentAuth'],
}

r = requesst.post(url, data = data, cookies = cookies)
print(r.text)