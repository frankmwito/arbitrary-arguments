# accept any number of keyword arguments and print out each key-value

def key_value(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(key_value(name = "franklyne",
                city = "nairobi",
                state = "Embakasi"))