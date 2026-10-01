#User class definition and registration
class User:
    def __init__(self,user_name,email,pass_word='12345'):
        self.user_name = user_name
        self.email = email
        self.pass_word = pass_word
    def print(self):
        print(self.user_name,self.email,end='')
    def is_gmail(self):
        return self.email.endswith('@gmail.com')

users = []

while True:
    u = input('username:')
    if u == '0': 
        print('************************')
        break
    e = input('email:')
    p = input('password:')

    user = User (pass_word=p,user_name=u,email=e)
    users.append(user)

print('All Users =',len(users))
for user in users:
    user.print()
    print(' Is Gmail:','YES' if user.is_gmail() else 'NO',sep='')
print(f'We Have {len(users)} Users Completed Their Information')