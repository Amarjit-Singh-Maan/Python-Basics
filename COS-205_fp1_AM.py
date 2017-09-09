# Amarjit Maan
# COS 205, Python Programming
# Problem # 1

def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    score = [0,0,0,0,0,0,0,0,0,0,0] # Initialization
    student = 0
    for i in infile:
        try:
            score[int(i)] = score[int(i)] + 1
        except:
            print("Char is not digit")
        print(score)
    infile.close()
    
main()
