from random import choice
def gen(c,n):
    b = ""
    for i in range(n):
        b += choice(c)
    return b
if __name__ == "__main__":
    pass_len = int(input("Enter password length: "))
    chars = ("Q W E R T Y U I O P A S D F G H J K L Z X C V B N M e r t y u i o p a s d f g h j k l z x c v b n m 1 2 3 4 5 6 7 8 9 0 ! @ # $ % & * ( ) _ + = ").split(" ")
    v=gen(chars,pass_len)
    with open("password.txt", "w") as file:
        
        file.write(v)
    print("\n******** Password generated ********")