# function that takes a name as a positional argument and any number of hobbies as *args

def name_hobbies(name, *args):
    hobbies = ', '.join(args)
    print(f"Hello my name is {name} and i like {hobbies}")
    
print(name_hobbies("frank", "basketball", "walk", "buying sneakers"))