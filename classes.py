from database_class import UserDatabase, TokenDatabase

from exceptions import UserNotAllowedError

class User:

    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password

class Token:

    def __init__(self, code, user:User, created_at=None):
        self.code = code
        self.user = user
        self.created_at = created_at


        @property
        def is_expired(self):
            pass

class TokenManager(TokenDatabase):

    def get_or_create_token(self, user) -> str:

        #Pesquisa pelo token do user ou cria um novo e salvar no banco
        #retorna um token válido
        if TokenDatabase.select_user_id(user):
            return True

        return "!@#!DSADQ!@#!@#"

    def verify_token(self, token_code) -> User:

        #verificar se o token informado pertence a um usuário
        #caso True, retorna os dados do User
        #caso False, retornar uma Exception

        if TokenDatabase.select(token_code):
        
            try:
                if self.get_or_create_token == True:
                    return UserDatabase.select()
            except Exception as err:
                return {"error": str(err)}, 600


class UserManager(UserDatabase):

    def add_new_user(self, username, password):

        self.insert(username, password)

    def get_user(self, username):

        result_list = self.select(username)

        return [
            User(
                id=item[0],
                username=item[1],
                password=item[2]
            )
           for item in result_list
        ]

    def get_user_token(self, username, password):

        try:

            user = self.get_user(username)[0]
            if user.username == username:
                if user.password == password:
                    return "!@#!DSADQ!@#!@#"

        except:
            pass

        raise UserNotAllowedError("Username ou Password Incorretos")






