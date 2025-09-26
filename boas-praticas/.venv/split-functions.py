## Com função

def is_prime_number(a: int) -> bool:    #type hint
    return bool(a % 2)


def main():
    print(is_prime_number(11))


if __name__ == "__main__":
    main()






## Sem função
#a = 11

#result = a % 2 

#print (f"rest:{result}")

#if result == 0:
#    print("Its not prime")
#else:
#    print("Its prime")