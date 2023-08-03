def validate_password(password):
    upper = False
    lower = False
    digit = False
    
    if "" in password:
        return False
    if len(password) < 8:
        return False
    
    if i in password:
        if (i.isupper()):
            upper = True
        elif(i.islower()):
            lower = True
            
            if upper and lower and digit:
                return True