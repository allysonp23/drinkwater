class Usuario():
    def __init__(self, nome, email, peso, password ):
        self.__nome = nome
        self.__email = email
        self.__peso = peso
        self.__password = password
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
        
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso
    
    @property
    def password(self):
        return self.__password
    
    @nome.setter
    def password(self, password):
        self.__password = password