exam_version = 11
#TODO 0A: your name

# Exam instructions
    # Outside assistance such as using AI or other people's assistance is not allowed; those caught will fail the class and be referred to the academic honesty board.
    # Don't change any lines labeled "DO NOT CHANGE THIS LINE"
    # This exam has 12 tasks, each worth the same amount. Plan on about 4 minutes per task so you have a few minutes at the end to turn it in.
    # If you are unable to do a task in 4 minutes, get as far as you can and then move on.
    # Comment out lines which cause the code to crash
    

def print_1():	#DO NOT CHANGE THIS LINE 
    
    #TODO 1A
    # print to the screen 'Welcome to my Recumbent Skateboard store'
  
    
def fix_prices_2(buy_price, sell_price):	#DO NOT CHANGE THIS LINE
    # Two prices will be passed in as the argument variables buy_price and sell_price
    # the type of buy_price and sell_price could be int, float or string - but you don't know which 
    # Your code should work for any valid combination
    
    #TODO 2A 
    # Change the buy_price and sell_price variables to both be float type
    buy_price = 0
    sell_price = 0
    

    return(buy_price, sell_price)	#DO NOT CHANGE THIS LINE
    
def calculate_profit_3(buy_price, sell_price):		#DO NOT CHANGE THIS LINE
    
    #TODO 3A
    # Two prices will be passed in as the argument variables buy_price and sell_price
    # assume they are float type.
    # The profit is the sell_price minus the buy_price and then multiplied by 0.97 (to account for credit card processing fees.)
    # calculate the profit and save in the variable profit
    profit = 0

    return(profit)	#DO NOT CHANGE THIS LINE
    
def set_barcode_4(product_name):	#DO NOT CHANGE THIS LINE
      
    #TODO 4A
    # Determine the barcode number for a product:
    # One string will be passed in as the argument variable product_name
    # Prompt the user for product_name's purchase number
    # and save the result as a integer in the variable prod_num: 
    # "What is product_name's purchase number?"
    #   Use this exact prompt but substitute the actual name of the product for 'product_name'
    #   Don't print the quotation marks
    #   Only use one line for this prompt 
    #   Do not leave a space between the apostrophe and the 's'
   
    prod_num = ""
    
    
    #TODO 4B
    # The barcode prefix is the store the number 3 represented in binary
    # calculate this and save in variable 'prefix' as a string
    prefix = "0000"


    return(prod_num, prefix)  #DO NOT CHANGE THIS LINE

def check_inventory_5(inventory_amount, order_amount):    #DO NOT CHANGE THIS LINE
    
    #TODO 5a
    # A purchase request has come in! Let's see if the store has enough inventory:
    # check : is 'inventory_amount' greater than or equal to 'order_amount' ?
    # save the result as a boolean in the variable 'have_enough'
    # assume 'inventory_amount' and 'order_amount' are integer types
    # you do not need to use 'if' statements to solve this, but it is allowed
    have_enough = True
    
       

    #TODO 5b
    # Decide if it's time to order more inventory.
    # Save as a boolean in variable 'reorder' TRUE when
    #    order_amount is greater than inventory_amount
    # or
    #    'inventory_amount' minus 'order_amount' is less than 10   
    # you do not need to use 'if' statements to solve this, but may if you wish
    reorder = False

    return(have_enough, reorder)  #DO NOT CHANGE THIS LINE


def set_sale_6(days_since, last_sale):           #DO NOT CHANGE THIS LINE           
    # assume the 'days_since' and 'last_sale' argument variables are integers
    
    #TODO 6a
    # Let's have a sale! If the days_since variable is even, set the sale_percent variable to the integer 22
    sale_percent = 0
    

    #TODO 6b
    #else, if the last_sale is not equal to 7 or 19, set the sale_percent to 13

    #TODO 6c
    #else set the sale percent to whichever number is larger: days_since or last_sale


    return(sale_percent) #DO NOT CHANGE THIS LINE


def user_choice_loop_7():           #DO NOT CHANGE THIS LINE          
    
    print_1() #DO NOT CHANGE THIS LINE
    choice_text = "[f]ix prices, [c]alc profits, set [b]arcode, [i]nventory check, [s]et sale, or [q]uit:" #DO NOT CHANGE THIS LINE
    
    #TODO 7a
    # Prompt the user with the 'choices_text' variable text until they input 'q'
    # you do not need to handle capitalizations or extra spaces
    # for purposes of this exam, don't actually call any of the functions the user requests
    
    loop_count = 0
   

    #TODO 7b
    # Let's track productivity!
    # Starting at 0 each time this function runs, count up how many times the loop runs (including the quit loop)
    # and save it in the variable loop_count
    # and then print out then number (instead of the word 'loop_count') when the user quits:
    # "You did loop_count things. see you later"
   # loop_count = 0 
    return(loop_count) #DO NOT CHANGE THIS LINE


def main(): 			        #DO NOT CHANGE THIS LINE
   
    # this program will run from a 'user choice loop' you'll build inside user_choice_7
    # but for testing and development purposes, here we'll call each of the functions
    # in sequence.
    # Nothing in Main will be graded, so you can use this to help with debugging 
    

    print("----Running print_intro_1...")
    print_1()
   
    print("----Running data_type_2()....")
    print("returns: ", fix_prices_2(1, "3") )
    
    print("----Running calculate_profit_3()....")
    print("returns: ", calculate_profit_3(1.0, 2.0))
    
    print("----Running set_barcode_4() ...")
    print("returns: ", set_barcode_4("E-Bike") )

    print("----Running check_inventory_5()...")
    print("returns: ", check_inventory_5(10,5))

    print("----Running set_sale_6()...")
    print("returns: ", set_sale_6(3, 20))
    
    print("---- user_choice_loop_7()...")
    user_choice_loop_7()



# END OF EXAM 
##########################################################################

def get_version():			#DO NOT CHANGE THIS LINE
    return exam_version		#DO NOT CHANGE THIS LINE

if __name__ == "__main__":	#DO NOT CHANGE THIS LINE
    #Encode in base 64 the architecture used #DO NOT CHANGE THIS LINE
    main()					#DO NOT CHANGE THIS LINE
