from collections import ChainMap


class UserProfile:
    def __init__(self, display_name: str):
        self.display_name = display_name

    def __getitem__(self, item: str):
        try:
            return getattr(self, item)
        except AttributeError:
            raise KeyError(item)


class UserAccount:
    def __init__(self, id: str, balance: int):
        self.id = id
        self.balance = balance

    def __getitem__(self, item: str):
        try:
            return getattr(self, item)
        except AttributeError:
            raise KeyError(item)


user_p = UserProfile("Jan Kowalski")
user_a = UserAccount("6327GHUDS", 3000)
user = ChainMap(user_p, user_a)
print(f"name = {user['display_name']}")
print(f"id = {user['id']}")
print(f"balance = {user['balance']}")


