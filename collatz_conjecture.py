import matplotlib.pyplot as plt

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