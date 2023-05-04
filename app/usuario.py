class Usuario():
    def __init__(self, nome, email, peso, password ):
        self.__nome = nome
        self.__email = email
        self.__peso = peso
        self.__passwrod = password
    
    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, email):
        self.__email = email
        
    @property
    def peso(self):
        return self.peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso
    
    @property
    def password(self):
        return self.password
    
    @nome.setter
    def password(self, password):
        self.__password = password