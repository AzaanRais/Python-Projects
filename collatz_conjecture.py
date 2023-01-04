import matplotlib.pyplot as plt

'''
this program creates the famous Collatz Conjecture, which is also known as 3n+1,
any random starting number is taken, if it is even, it is divided by 2, else it is multiplied by 3 and 1 is added to the product - this cycle is repeated and for every number, this cycle eventually gets stuck in a loop of 4-2-1 (this has been tested till 2^68, but this conjecture is not proven true yet)

example:
3 -> 3, 10, 5, 16, 8, 4, 2, 1....
'''

def main():
    inp = int(input("Enter number: "))
    if inp >= 1:
        collat(inp)
    else:
        print("no")

def collat(n):
    conjecture = [n] 
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            conjecture.append(round(n))
        else:
            n = (3 * n) + 1
            conjecture.append(round(n))

    print(f"{conjecture} \nSteps taken: {len(conjecture) - 1} \nMaximum value: {max(conjecture)}")

    x_axis = [i for i in range(len(conjecture))]

    plt.plot(x_axis, conjecture, color='red')
    plt.title("Collatz Conjecture")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()            