base = int(input("Enter a base"));
power = int(input("Enter power"));

i = 1;
ans = 1;

while i<=power:
    ans = ans * base;
    i = i+1;


print("Final answer is" , ans); 