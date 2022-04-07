from unicodedata import name


class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    allergies = ''
    food_diet = ''
    user_type = ''
    is_active = ''

    def get_full_name(self):
        return "{}, {}".format(user.first_name, user.last_name)

class MenuItem():
    name = ''
    description = ''
    serving_size = ''
    allergens = ''


class Order():
    price = ""
    meal_type = ""
    user_name = ""

    def get_order_details(self):
        return  "{}, at GHS {}, type: {}".format(order.user_name, order.price ,order.meal_type)
    


    # def get_order_details(self):
    #     return "{} {}".format(order.user_name, order.price ,order.meal_type)


class Price():
    no_pack = ""
    

user = User()
user.first_name = 'Ini'
user.last_name = 'Arthur'
user.phone_number = '8723438887'
user.email_address = 'ini.arthur@meltwater.org'

print('My name is {} and we are Fuudia'.format(user.get_full_name()))


order = Order()
order.meal_type = 'Breakfast'
order.user_name = 'Arthur'
order.price = 'GH30'

print('Order accepted for {}'.format(order.get_order_details()))

class Father():
    last_name = ''
    company = ''
    wife = ''
class Son(Father):
    first_name = ''