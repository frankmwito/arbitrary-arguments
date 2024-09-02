# return a mix of positional arguments and arbitrary arguments

def mix(name, *args, **kwargs):
    nick_names = ', '.join(args)
    print(f"Hello {name} your nick names are: {nick_names}")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print(mix("frank","my G", "you guy my guy",
                city = "nairobi",
                state = "Embakasi"))