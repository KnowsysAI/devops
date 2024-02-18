import requests
url = "https://search-newsdata-tester-uy43guqnasvykkyt5wkmx4y7sa.us-east-1.es.amazonaws.com/ukraine_index/_search"
username = "ethanfincher"
password = "Password123!"
response = requests.get(url, auth=(username, password))
print(response.status_code)
print(response.json())


# if command == "c":
#     print("bark")
# elif command == "r":
#     print("herro")
# elif command == "u":
#     print("woof")
# elif command == "d":
#     print("pew pew")
# elif command == "q":
#     print("grrrrr")
# command = input('enter an operation: ').lower()

# while(command not in ("c", "r", "u", "d", "q")):
#     command = input('please enter a valid operation: ').lower()