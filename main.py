import random


def main():
    i=0
    total = 0
    numbers = [0]*5
    while i<5:
        numbers[i]=random.randint(0,100)
        i=i+1
    for z in numbers:
        total+=z
        if total <100:
    
            continue
        else:
            total=total-z
            break

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
