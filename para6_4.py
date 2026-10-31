try:
    try:
        print("Start")
        print(vasya)
        print("No errors")
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)
