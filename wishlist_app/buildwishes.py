from datetime import date
from linearbag import Bag
from Wish import Wish
from user import User
from linearmap import Map

# get wishes from user
# create Wish objects
# add each Wish obj to Bag in linearbag.py
# add user and wishes to map

def main() :
    name = input('Type your name: ')
    email = input('Your email address: ')
    password = input('Your password: ')
    new_user = User(name, email, password)
    print(new_user)

    wish = get_user_wish()
    bag = Bag()
    while True :
        if wish is None :
            break
        bag.add(wish)
        wish = get_user_wish()
    mywishlist = Map()
    mywishlist.add(new_user, bag)
    mywishes = mywishlist.valueOf(new_user)

    print('Hello '+new_user.name()+' here are your wishes')

    for item in mywishes :
        print(item)


def get_user_wish() :
    text = input('Type what you wish for: ')
    if text == '0' :
        return None
    return Wish(text)

main()