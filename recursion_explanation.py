import sys
import time
import hashlib

def get_ascii_table(characters):
    
    
    ascii_table_ordered = []
    
    if characters == "lower":
    
        #lowercase
        lowercase_ascii = [97,122]
        for i in range(max(lowercase_ascii) - min(lowercase_ascii) + 1):
            
            ascii_table_ordered.append(chr(min(lowercase_ascii) + i))
        
    elif characters == "upper":
        
         #lowercase
        lowercase_ascii = [97,122]
        for i in range(max(lowercase_ascii) - min(lowercase_ascii) + 1):
            
            ascii_table_ordered.append(chr(min(lowercase_ascii) + i))
        
        #uppercase   
        uppercase_ascii = [65, 90]
        for i in range(max(uppercase_ascii) - min(uppercase_ascii) + 1):
            
            ascii_table_ordered.append(chr(min(uppercase_ascii) + i))
            
    elif characters == "numbers":
        
        #lowercase
        lowercase_ascii = [97,122]
        for i in range(max(lowercase_ascii) - min(lowercase_ascii) + 1):
            
            ascii_table_ordered.append(chr(min(lowercase_ascii) + i))
        
        #uppercase   
        uppercase_ascii = [65, 90]
        for i in range(max(uppercase_ascii) - min(uppercase_ascii) + 1):
            
            ascii_table_ordered.append(chr(min(uppercase_ascii) + i))
        
        #number
        number_ascii = [48,57]
        for i in range(max(number_ascii) - min(number_ascii) + 1):
            
            ascii_table_ordered.append(chr(min(number_ascii) + i))
    
    elif characters == "all":
        
         #lowercase
        lowercase_ascii = [97,122]
        for i in range(max(lowercase_ascii) - min(lowercase_ascii) + 1):
            
            ascii_table_ordered.append(chr(min(lowercase_ascii) + i))
        
        #uppercase   
        uppercase_ascii = [65, 90]
        for i in range(max(uppercase_ascii) - min(uppercase_ascii) + 1):
            
            ascii_table_ordered.append(chr(min(uppercase_ascii) + i))
        
        #number
        number_ascii = [48,57]
        for i in range(max(number_ascii) - min(number_ascii) + 1):
            
            ascii_table_ordered.append(chr(min(number_ascii) + i))
        
        #special characters    
        special_ascii1 = [33,47]
        for i in range(max(special_ascii1) - min(special_ascii1) + 1):
            
            ascii_table_ordered.append(chr(min(special_ascii1) + i))
            
        special_ascii2 = [58,64]
        for i in range(max(special_ascii2) - min(special_ascii2) + 1):
            
            ascii_table_ordered.append(chr(min(special_ascii2) + i))
            
        special_ascii3 = [91,96]
        for i in range(max(special_ascii3) - min(special_ascii3) + 1):
            
            ascii_table_ordered.append(chr(min(special_ascii3) + i))
            
        special_ascii4 = [123,126]
        for i in range(max(special_ascii4) - min(special_ascii4) + 1):
            
            ascii_table_ordered.append(chr(min(special_ascii4) + i))
        
    return ascii_table_ordered

ascii_table_lower = get_ascii_table("lower")
ascii_table_upper = get_ascii_table("upper")
ascii_table_numbers = get_ascii_table("numbers")
ascii_table_all = get_ascii_table("all")

test_hash = "900150983cd24fb0d6963f7d28e17f72"

def brute_force(ascii_list, hashed_pwd):
    
    index_counter = [0]
    while True:
        
        index_counter[0] += 1
    
      
        carry_over = 0
        while index_counter[carry_over] == len(ascii_list):
        
            
            carry_over += 1
            
            if carry_over == len(index_counter):
                index_counter.append(0)
            
            index_counter[carry_over] += 1 
            index_counter[carry_over - 1] = 0
            
        hash_string = ""    
            
        for i in index_counter:
            
            hash_string += ascii_list[i]
            
        #turn hash_string to md5 hash
        guess = hashlib.md5(hash_string.encode()).hexdigest()
        
        #if statement
        if guess == hashed_pwd:
            print("found", hash_string)
            
            break
        #print(hash_string)
        
brute_force(ascii_table_lower, "5f4dcc3b5aa765d61d8327deb882cf99")