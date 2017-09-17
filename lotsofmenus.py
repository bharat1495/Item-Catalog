from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuapp.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
U1 = User(name="Sunny", email="sunnysingh@gomail.com",
             picture='http://www.youthconnect.in/wp-content/uploads/2013/11/Sachin-Tendulkar.jpg')
session.add(U1)
session.commit()

# Menu for Food Point
restaurant1 = Restaurant(user_id=1, name="Food Point")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Amritsari Kulcha", price="Rs 60",course="Starters", restaurant=restaurant1)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Paneer Tikka", price="Rs 120",course="Starters", restaurant=restaurant1)
session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chicken Biryani", price="Rs 130",course="Main Course", restaurant=restaurant1)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Butter Naan", price="Rs 25",course="Main Course", restaurant=restaurant1)
session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Yellow Dal", price="Rs 75",course="Main Course", restaurant=restaurant1)
session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Kadahi Paneer", price="Rs 110",course="Main Course", restaurant=restaurant1)
session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Gulab Jamun", price="Rs 30",course="Dessert", restaurant=restaurant1)
session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Ice Cream", price="Rs 40",course="Dessert", restaurant=restaurant1)
session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Mango Lassi", price="Rs 30",course="Beverage", restaurant=restaurant1)
session.add(menuItem9)
session.commit()

menuItem10 = MenuItem(user_id=1, name="Juice", price="Rs 20",course="Beverage", restaurant=restaurant1)
session.add(menuItem10)
session.commit()


# Menu for Jaggi Sweets
restaurant2 = Restaurant(user_id=1, name="Jaggi Sweets")
session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Mushroom Tikka", price="Rs 130",course="Starters", restaurant=restaurant2)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Malai Chaap", price="Rs 130",course="Starters", restaurant=restaurant2)
session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Veg Biryani", price="Rs 120",course="Main Course", restaurant=restaurant2)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Lachha Parantha", price="Rs 20",course="Main Course", restaurant=restaurant2)
session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Dal Makhni", price="Rs 80",course="Main Course", restaurant=restaurant2)
session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Paneer Butter Masala", price="Rs 140",course="Main Course", restaurant=restaurant2)
session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Moong Halwa", price="Rs 55",course="Dessert", restaurant=restaurant2)
session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Ice Cream with Brownie", price="Rs 50",course="Dessert", restaurant=restaurant2)
session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Blue Mint", price="Rs 60",course="Beverage", restaurant=restaurant2)
session.add(menuItem9)
session.commit()

menuItem10 = MenuItem(user_id=1, name="Virgin Mojito", price="Rs 45",course="Beverage", restaurant=restaurant2)
session.add(menuItem10)
session.commit()


# Menu for Sheetal Restaurant
restaurant3 = Restaurant(user_id=1, name="Neem Rana")
session.add(restaurant3)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Soya Chaap Tikka", price="Rs 190",course="Starters", restaurant=restaurant3)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Soya Rumali Rolls", price="Rs 190", course="Starters", restaurant=restaurant3)
session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Cheese Fingers", price="Rs 180",course="Main Course", restaurant=restaurant3)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Missi Roti", price="Rs 50",course="Main Course", restaurant=restaurant3)
session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Dal Panchrattan", price="Rs 160",course="Main Course", restaurant=restaurant3)
session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Rada Chicken", price="Rs 230",course="Main Course", restaurant=restaurant3)
session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Rasmalai", price="Rs 90",course="Dessert", restaurant=restaurant3)
session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Shaahi Tukda", price="Rs 110",course="Dessert", restaurant=restaurant3)
session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Masala Chhaachh", price="Rs 60",course="Beverage", restaurant=restaurant3)
session.add(menuItem9)
session.commit()

menuItem10 = MenuItem(user_id=1, name="Nimbu Pani", price="Rs 50",course="Beverage", restaurant=restaurant3)
session.add(menuItem10)
session.commit()


# Menu for Mainland China
restaurant4 = Restaurant(user_id=1, name="Mainland China")

session.add(restaurant4)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Corn Spinach Roll", price="Rs 120",course="Starters", restaurant=restaurant4)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Cheese Chilly", price="Rs 130",course="Starters", restaurant=restaurant4)
session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chicken Fried Rice", price="Rs 170",course="Main Course", restaurant=restaurant4)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Chilly Garlic Noodles", price="Rs 190",course="Main Course", restaurant=restaurant4)
session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Veg Dimsum",price="Rs 190", course="Main Course", restaurant=restaurant4)
session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Mushroom Chilly", price="Rs 180",course="Main Course", restaurant=restaurant4)
session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Haka Noodles", price="Rs 170",course="Dessert", restaurant=restaurant4)
session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Ice Cream", price="Rs 60",course="Dessert", restaurant=restaurant4)
session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Watermelon Slush", price="Rs 90",course="Beverage", restaurant=restaurant4)
session.add(menuItem9)
session.commit()

menuItem10 = MenuItem(user_id=1, name="Choco Frappe", price="Rs 80",course="Beverage", restaurant=restaurant4)
session.add(menuItem10)
session.commit()


# Menu for Yo China
restaurant5 = Restaurant(user_id=1, name="Yo China")

session.add(restaurant5)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Honey Cauliflower", price="Rs 130",
                     course="Starters", restaurant=restaurant5)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken Tikka", price="Rs 150",
                     course="Starters", restaurant=restaurant5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Fried Rice", price="Rs 120",
                     course="Main Course", restaurant=restaurant5)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Hakka Noodles", price="Rs 80",
                     course="Main Course", restaurant=restaurant5)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Manchurian with Gravy", price="Rs 70",
                     course="Main Course", restaurant=restaurant5)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Chilli Cheese", price="Rs 90",
                     course="Main Course", restaurant=restaurant5)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Coconut Bar", price="Rs 50",
                     course="Dessert", restaurant=restaurant5)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Cold Drink", price="Rs 40",
                     course="Beverage", restaurant=restaurant5)

session.add(menuItem8)
session.commit()


# Menu for Kababchi
restaurant6 = Restaurant(user_id=1, name="Kababchi")

session.add(restaurant6)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Veg Manchurian", price="Rs 100",
                     course="Starters", restaurant=restaurant6)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Soya Chaap", price="Rs 90",
                     course="Starters", restaurant=restaurant6)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chilli Paneer", price="Rs 110",
                     course="Main Course", restaurant=restaurant6)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Veg Noodles", price="Rs 120",
                     course="Main Course", restaurant=restaurant6)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Veg Manchurian with Gravy",
                     price="Rs 90", course="Main Course", restaurant=restaurant6)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Custard Tart", price="Rs 60",
                     course="Dessert", restaurant=restaurant6)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Cold Drink", price="Rs 40",
                     course="Beverage", restaurant=restaurant6)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Lemon Soda", price="Rs 40",
                     course="Beverage", restaurant=restaurant6)

session.add(menuItem8)
session.commit()


# Menu for Saffron
restaurant7 = Restaurant(user_id=1, name="Saffron")

session.add(restaurant7)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Sausage", price="Rs 80",
                     course="Starters", restaurant=restaurant7)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Mozarella Wings", price="Rs 70",
                     course="Starters", restaurant=restaurant7)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Pizza", price="Rs 200",
                     course="Main Course", restaurant=restaurant7)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Enchiladas", price="Rs 60",
                     course="Main Course", restaurant=restaurant7)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Cheese Cake", price="Rs 70",
                     course="Dessert", restaurant=restaurant7)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Ice Cream", price="Rs 70",
                     course="Dessert", restaurant=restaurant7)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Lemonade", price="Rs 50",
                     course="Beverage", restaurant=restaurant7)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Juice", price="Rs 40",
                     course="Beverage", restaurant=restaurant7)

session.add(menuItem8)
session.commit()


# Menu for Oregano
restaurant8 = Restaurant(user_id=1, name="Oregano")

session.add(restaurant8)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Cheese Bombs", price="Rs 100",
                     course="Starters", restaurant=restaurant8)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Pinwheels", price="Rs 90",
                     course="Starters", restaurant=restaurant8)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Casserole", price="Rs 100",
                     course="Main Course", restaurant=restaurant8)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Panini", price="Rs 60",
                     course="Main Course", restaurant=restaurant8)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Egg plant Roll", price="Rs 70",
                     course="Main Course", restaurant=restaurant8)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Cookies", price="Rs 40",
                     course="Dessert", restaurant=restaurant8)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Ice Cream", price="Rs 30",
                     course="Dessert", restaurant=restaurant8)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Hot Chocolate", price="Rs 50",
                     course="Beverage", restaurant=restaurant8)

session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Cold Coffee", price="Rs 60",
                     course="Beverage", restaurant=restaurant8)

session.add(menuItem9)
session.commit()

# Menu for Barbeque Nation
restaurant9 = Restaurant(user_id=1, name="Barbeque Nation")

session.add(restaurant9)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Bruschetta", price="Rs 90",
                     course="Starters", restaurant=restaurant9)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Italian Roll", price="Rs 110",
                     course="Starters", restaurant=restaurant9)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="White Pasta", price="Rs 140",
                     course="Main Course", restaurant=restaurant9)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Red Pasta", price="Rs 90",
                     course="Main Course", restaurant=restaurant9)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Ravioli", price="Rs 80",
                     course="Main Course", restaurant=restaurant9)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Cream Cake", price="Rs 100",
                     course="Dessert", restaurant=restaurant9)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Gelato", price="Rs 90",
                     course="Dessert", restaurant=restaurant9)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Hot Chocolate", price="Rs 70",
                     course="Beverage", restaurant=restaurant9)

session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Coffee", price="Rs 60",
                     course="Beverage", restaurant=restaurant9)

session.add(menuItem9)
session.commit()


# Menu for Grille
restaurant10 = Restaurant(user_id=1, name="Grille")

session.add(restaurant10)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Guacamole", price="Rs 70",
                     course="Starters", restaurant=restaurant10)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Nachos", price="Rs 50",
                     course="Starters", restaurant=restaurant10)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Tostada", price="Rs 90",
                     course="Main Course", restaurant=restaurant10)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Quinoa", price="Rs 70",
                     course="Main Course", restaurant=restaurant10)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Pinwheels", price="Rs 60",
                     course="Main Course", restaurant=restaurant10)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Capirotada", price="Rs 50",
                     course="Dessert", restaurant=restaurant10)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Churros", price="Rs 40",
                     course="Dessert", restaurant=restaurant10)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Hot Chocolate", price="Rs 50",
                     course="Beverage", restaurant=restaurant10)

session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Lemonade", price="Rs 40",
                     course="Beverage", restaurant=restaurant10)

session.add(menuItem9)
session.commit()


# Menu for Stuffd
restaurant11 = Restaurant(user_id=1, name="Stuffd")

session.add(restaurant11)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Guacamole", price="Rs 90",
                     course="Starters", restaurant=restaurant11)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Rice Balls", price="Rs 100",
                     course="Starters", restaurant=restaurant11)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Lasagna", price="Rs 150",
                     course="Main Course", restaurant=restaurant11)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Pasta Salad", price="Rs 60",
                     course="Main Course", restaurant=restaurant11)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Frittata", price="Rs 70",
                     course="Main Course", restaurant=restaurant11)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Trifles", price="Rs 50",
                     course="Dessert", restaurant=restaurant11)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Choco Taco", price="Rs 50",
                     course="Dessert", restaurant=restaurant11)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Mule", price="Rs 50",
                     course="Beverage", restaurant=restaurant11)

session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Juice", price="Rs 40",
                     course="Beverage", restaurant=restaurant11)

session.add(menuItem9)
session.commit()

# Menu for Chili
restaurant12 = Restaurant(user_id=1, name="Chili")

session.add(restaurant12)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Guacamole", price="Rs 120",
                     course="Starters", restaurant=restaurant12)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Enchilada Nachos", price="Rs 110",
                     course="Starters", restaurant=restaurant12)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Casserole", price="Rs 130",
                     course="Main Course", restaurant=restaurant12)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Mexican Mocha", price="Rs 150",
                     course="Main Course", restaurant=restaurant12)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Possole", price="Rs 140",
                     course="Main Course", restaurant=restaurant12)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Rice Pudding", price="Rs 70",
                     course="Dessert", restaurant=restaurant12)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Ice Cream", price="Rs 50",
                     course="Dessert", restaurant=restaurant12)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Margaritas", price="Rs 60",
                     course="Beverage", restaurant=restaurant12)

session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Horchata", price="Rs 50",
                     course="Beverage", restaurant=restaurant12)

session.add(menuItem9)
session.commit()

print "Added Restaurants and Menu Items!"
