
def fizz_buzz(no):
    if no % 3 == 0:
        if no % 5 == 0:
            return "FizzBuzz"
        return "Fizz"

    elif no % 5 == 0:
        return "Buzz"
    else:
        return no    

