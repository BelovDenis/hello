# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
q=[3,4,5,0,4,21,68,34,17,23,5,10,12]
for i in range(len(q)):
    for j in range(i+1,len(q)):
        for k in range(j+1,len(q)):
            a=q[i]
            b=q[j]
            c=q[k]
            if a+b>c and a+c>b and b+c>a:
                p=(a+b+c)/2
                S=(p*(p-a)*(p-b)*(p-c))**(1/2)
                max=0
                if S>max:
                    max=S
print (max)