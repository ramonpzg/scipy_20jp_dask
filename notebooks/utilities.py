import os



def check_or_add(old_path, *args):
    
    """
    This function will help us check whether one or more directories exists, and
    if they don't exist, it will create, combine, and return a new directory.
    """
        
    if not os.path.exists(os.path.join(old_path, *args)):
        os.makedirs(os.path.join(old_path, *args))

    return os.path.join(old_path, *args)



