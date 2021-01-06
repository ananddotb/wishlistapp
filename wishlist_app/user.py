class User :
    def __init__(self, name, email, password) :
        self._name = name
        self._email = email
        self._password = password
    
    def add_wishlist(self, wishlist) :
        self._wishlist = wishlist
    
    def wishlist(self) :
        return self._wishlist
    
    def name(self) :
        return self._name
    

    def email(self) :
        return self._email
    
    def password(self) :
        return self._password
    
    def __str__(self) :
        return '%15s%15s%10s' % (self._name, self._email, self._password)
    

    