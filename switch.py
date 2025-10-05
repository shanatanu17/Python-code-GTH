print("1.addition");
print("2.subtarction");

a = int(input("Enter value for a"));
b = int(input("Enter value for b"));

choice = int(input("Enter the choice "));



match choice:
  
  case 1:
    c = a+b;
    print(c);

  case 2:
    d = a-b;
    print(d);

  case _:
   print("Wrong choice");

