from edapi import EdAPIWL

ed = EdAPIWL()
ed.login()

user_info = ed.get_user_info()
user = user_info["user"]

print(f"Hello {user['name']}!")
