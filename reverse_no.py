


no = 123;
rev = 0;


while no !=0 :
  ld = no % 10;
  rev = rev * 10 + ld;
  no = no // 10;

print(" Reverse of a number is " , rev);