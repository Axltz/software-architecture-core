import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
    
class UserRepository:
    def __init__(self):
        self._users = []
    
    def emailExist(self, email: str) -> bool:
        for user in self._users:
            if user.email == email:
                return True
        return False
    
    def userExist(self, email: str):
        for user in self._users:
            if user.email == email:
                return user
        return None

    def saveUser(self, user: User):
        self._users.append(user)
    
    def get_all(self):
        return self._users
    

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository


    def createUser(self, name: str, email: str, password: str):
        if (self.repository.emailExist(email)) is not None:
            raise ValueError("Email already exist")

        password_hash = hash_password(password)
        user = User(name, email, password_hash)

        self.repository.saveUser(user)
        return user
    
    def login(self, email: str, password: str):
        
        user = self.repository.userExist(email)

        if user is None:
            return False
        
        if user.password == hash_password(password):
            return True
        
        return False
        

repo = UserRepository()
service = UserService(repo)

service.createUser("Axel", "axel@gmail.com", "1234")
service.createUser("Endrick", "newPele@gmail.com", "abcd")

#ValueError
print(service.login("axel@gmail.com", "1234"))    # True
print(service.login("axel@gmail.com", "xxxx"))    # False
print(service.login("no@existe.com", "1234"))     # False

service.createUser("Gavi", "axel@gmail.com", "#####")

