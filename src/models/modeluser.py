

class ModelUser():
    
    @classmethod
    def login(self,db,user):
        from .user import User
        try:
            cursor = db.cursor()
            cursor.execute("SELECT id,username,password FROM login WHERE username = '{}'".format(user.username))

            row = cursor.fetchone()
            if row != None:
                user = User(row[0],row[1],User.check_password(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        