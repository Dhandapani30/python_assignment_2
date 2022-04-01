def FizzBizz(n):
    print("Fizz") if n%3==0 and n%5!=0 else (print("Bizz") if n%3!=0 and n%5==0 else (print("FizzBizz") if n%3==0 and n%5==0 else print(n)))
FizzBizz(6)
