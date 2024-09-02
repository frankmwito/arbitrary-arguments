# accept arbitrary keyword arguments for personal information and return formatted string

def greet(**kwargs):
    info = ', '.join(f"{key}: {value}" for key, value in kwargs.items())
    print(f"Hello! Here is the information you provided: {info}")


result = greet(name = "franklyne",
      age = "34",
      city = "new york")

print(result)