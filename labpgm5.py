import sys
if __name__ == "__main__":
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    simple_interest = (principal * rate * time) / 100
    print("Simple interest is: ", simple_interest)
    
