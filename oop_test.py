class ascii_table:
        
    
    def get_ascii_table(self, characters):
    
    
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