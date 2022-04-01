def speed(s):
    if s<70:
        print("Ok")
    else:
        print("demerit_points=", int((s-70)//5))
speed(80)
