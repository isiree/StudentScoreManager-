# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953631
# Date: 1/12/2022

stud_id_count=0 #counts the no. of time student ids are entered
list_id=[]#stores all the student ids entered
ptfour_dict=dict()
def get_student_id():

    while True:
        global list_id,stud_id_count
        student_id=input("\nPlease enter your student ID:")
        stud_id_count+=1 #counts the no. of student ids entered

        if student_id in list_id[:int(stud_id_count-1)]:
            print("This student ID has already been entered. Please enter a unique ID")
            continue #continues to the begining if student id is repeated
        elif student_id=="":
            print("student ID cannot be empty . Please re-enter")
            continue
        elif student_id[0]!="w" or student_id[1:].isdigit()==False or len(student_id)!=8:#id must start with 0 and id must have digits as its last 7 characters and id must have 8 charcters in total.
            print("Please enter valid student ID , eg.w1234567")
        else:
            list_id.append(student_id)#append the student id to a list to be used to check id repetitions
            return student_id

def get_pass1():
    while True:
        try:
            Pass=int(input("\nEnter your credits at pass:"))
        except ValueError:#if a non integer is entered , will reprompt for input until its given correctly
                print("integer required")
        else:
            return Pass

def get_defer1():
    while True:
        try:
            defer=int(input("Enter your credits at defer:"))
        except ValueError:#if a non integer is entered , will reprompt for input until its given correctly
                print("integer required")
        else:
            return defer

def get_fail1():
    while True:
        try:
            fail=int(input("Enter your credits at fail:"))
        except ValueError:#if a non integer is entered , will reprompt for input until its given correctly
                print("integer required")
        else:
            return fail

def get_pass2():
    while True:
        try:
            Pass=int(input("\nEnter your total PASS credits:"))
        except ValueError:#if a non integer is entered , will reprompt for input until its given correctly
                print("integer required")
        else:
            return Pass

def get_defer2():
    while True:
        try:
            defer=int(input("Enter your total DEFER credits:"))
        except ValueError:#if a non integer is entered , will reprompt for input until its given correctly
                print("integer required")
        else:
            return defer

def get_fail2():
    while True:
        try:
            fail=int(input("Enter your total FAIL credits:"))
        except ValueError:#if a non integer is entered , will reprompt for input until its given correctly
                print("integer required")
        else:
            return fail

def histogram(Progress,mod_trailer,mod_retriever,Exclude,i):

    print("\nHistogram\n")
    print(f"Progress {Progress} : " + "*" * int(Progress))#prints "*" for the no. of times "progress" is recorded , horizontaly
    print(f"Trailer {mod_trailer} : " + "*" * int(mod_trailer))
    print(f"Retriever {mod_retriever} : " + "*" * int(mod_retriever))
    print(f"Excluded {Exclude} : " + "*" * int(Exclude))
    print(f"\n{i} outcomes in total.")#total no. of outcomes recorded.

def pttwo_list(list_pro,listtra_max,listretri_max,listexc_max):
    print("\nPart 2:\n")
    for i in range(len(list_pro)):
        print("Progress-",str(list_pro[i])[1:-1])#removes the brackets after converting list element to str
    for i in range(len(listtra_max)):
        print("Trailer-",str(listtra_max[i])[1:-1])
    for i in range(len(listretri_max)):
        print("Retriever-",str(listretri_max[i])[1:-1])
    for i in range(len(listexc_max)):
        print("Excluded-",str(listexc_max[i])[1:-1])

    return list_pro,listtra_max,listretri_max,listexc_max

def ptthree_textfile(list_pro,listtra_max,listretri_max,listexc_max):

    textfile1=open(r"progrssion_data.txt","w")#open new file to write
    for i in range(len(list_pro)):#write as iterationg though the list
        textfile1.write("\rProgress-"+str(list_pro[i])[1:-1])
    for i in range(len(listtra_max)):
        textfile1.write("\rTrailer-"+str(listtra_max[i])[1:-1])
    for i in range(len(listretri_max)):
        textfile1.write("\rRetriever-"+str(listretri_max[i])[1:-1])
    for i in range(len(listexc_max)):
        textfile1.write("\rExcluded-"+str(listexc_max[i])[1:-1])
    textfile1.close()
    textfile1=open(r"progrssion_data.txt","r")#reopen the file for reading
    data=textfile1.read()
    print("\nPart 3:")
    print(data)
    textfile1.close()



