a = int(input("Enter the value of a "));
b = int(input("Enter the value of b "));

print("Values before swapping ");
print("a = "  , a  , " b = " , b);


a = a + b;
b = a-b;
a = a - b;


print("Values After swapping ");
print("a = "  , a  , " b = " , b);
