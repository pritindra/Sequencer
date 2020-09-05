import sys

patt = input("Enter the pattern::")
inp = input("Enter the inputs::")

def split(l):
    return list(l)

patt_list = split(patt)
inp_list = split(inp)

temp = []

choice = input("Do you want to print output in a text file ?[y/n]")

if choice == "y":
    file = open('output.txt', 'w')
    sys.stdout = file
    for p in range(len(patt_list)):
                
        for s in range(len(patt_list)):
            temp.insert(s,patt_list[s])

        for q in range(len(inp_list)):
            
            st = ""
            temp[p] = inp_list[q]
            print(st.join(temp))
        del temp[:]

    output = (p+1)*(q+1)
    print("No. of Outputs::" + str(output))
        
    file.close()

else:
    for p in range(len(patt_list)):
                
        for s in range(len(patt_list)):
            temp.insert(s,patt_list[s])

        for q in range(len(inp_list)):
            
            st = ""
            temp[p] = inp_list[q]
            print(st.join(temp))
        del temp[:]

    output = (p+1)*(q+1)
    print("No. of Outputs::" + str(output))
