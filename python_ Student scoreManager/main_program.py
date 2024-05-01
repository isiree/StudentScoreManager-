# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953631
# Date: 1/12/2022

Progress=0#counter for no. of times progress is recorded
mod_trailer=0#counter for no. of times module trailer is recorded
mod_retriever=0#counter for no. of times retriever is recorded
Exclude=0#counter for no. of times exclude is recorded
list_pro=[]
list_trailer=[]
list_retri=[]
list_exc=[]
ptfour_dict=dict()
credit_type=[] #stores a string with progression data to use as value in dictionary
i=0#variable for outcome/iteration counter for every new student record .
def main():
    global Progress,mod_trailer,mod_retriever,Exclude
    while True:
        print("\nPlease enter '1' for student version\nPlease enter '2' for staff version""")
        option=input(">>>")
        if option =="1":
            progression_outcome1()#gives the outcome for the relevent credits per student record
            break
        elif option =="2":
            sub_main()#contains all main executions
            break
        else:
            print("\nPlease enter valid input as instructed.")
            continue

def sub_main():
    progression_outcome2()#gives the outcome for the relevent credits per student record
    global i
    i+=1#counts the number of outcomes(student records)
    if_correct_input()#if correct input is given to the question continues with the program or repeats question

def if_correct_input():

    command=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")#the question

    if command=="y":
        sub_main()#re-run the program to enter more data
    elif command=="q":
        menu()#gives multiple choices to display output and to end .
    else:
        print("\nplease enter valid input")
        if_correct_input()#repeats till correct input is given


def progression_outcome2():
    import operations
    student_id=operations.get_student_id()
    while True:
        Pass=operations.get_pass2()#cheks for valid int input and returns
        if Pass not in [0,20,40,60,80,100,120]:#can only accept these credits
                print("out of range")
                continue
        else:
            break
    while True:
        defer=operations.get_defer2()#cheks for valid int input and returns
        if defer not in [0,20,40,60,80,100,120]:#can only accept these credits
                print("out of range")
                continue
        else:
            break

    while True:
        fail=operations.get_fail2()#cheks for valid int input and returns
        if fail not in [0,20,40,60,80,100,120]:#can only accept these credits
                print("out of range")
                continue
        else:
            break

    outcome(Pass,defer,fail,student_id)#checks and records the progression type(eg.progress ,trailing,etc)

def progression_outcome1():
    import operations
    student_id=None
    while True:
        Pass=operations.get_pass1()#cheks for valid int input and returns
        if Pass not in [0,20,40,60,80,100,120]:#can only accept these credits
                print("out of range")
                continue
        else:
            break
    while True:
        defer=operations.get_defer1()#cheks for valid int input and returns
        if defer not in [0,20,40,60,80,100,120]:#can only accept these credits
                print("out of range")
                continue
        else:
            break

    while True:
        fail=operations.get_fail1()#cheks for valid int input and returns
        if fail not in [0,20,40,60,80,100,120]:#can only accept these credits
                print("out of range")
                continue
        else:
            break
    outcome(Pass,defer,fail,student_id) #checks and records the progression type(eg.progress ,trailing,etc)

def outcome(Pass,defer,fail,student_id):
    total=Pass+defer+fail
    global Progress,mod_trailer,mod_retriever,Exclude
    global list_pro,list_trailer,list_retri,list_exc
    global ptfour_dict,credit_type
    if total !=120:
        global i
        i-=1 #if total is not equal to 120 the credits for that outcome are not counted in the "no. of outcomes".
        print("Total Incorrect")
    elif Pass==120:
        Progress+=1#counts the times 'progress' is recorded
        tuple_pro=Pass,defer,fail #store the credits related to the progression outcome in a tuple
        list_pro.append(tuple_pro)# creates  a nested list containing all values entered relevent to progression outcome
        credit_type=f"Progress - {Pass},{defer},{fail}" #value for dictionary
        ptfour_dict.update({student_id:credit_type})#stores student id and credit type as key value pairs in dict. respectivly.
        print("Progress")
    elif 120>Pass>80:
        mod_trailer+=1#counts the times 'module trailer' is recorded
        tuple_tra=Pass,defer,fail#store the credits related to the progression outcome in a tuple
        list_trailer.append(tuple_tra)# creates  a nested list containing all values entered relevent to progression outcome
        credit_type=f"Progress (module trailer) - {Pass},{defer},{fail}"
        ptfour_dict.update({student_id:credit_type})
        print("Progress (module trailer)")
    elif fail<80:
        mod_retriever+=1#counts the times 'module retriever' is recorded
        tuple_retri=Pass,defer,fail#store the credits related to the progression outcome in a tuple
        list_retri.append(tuple_retri)# creates  a nested list containing all values entered relevent to progression outcome
        credit_type=f"Do not progress - module retriever - {Pass},{defer},{fail}"
        ptfour_dict.update({student_id:credit_type})
        print("Do not progress - module retriever")
    elif fail>=80:
        Exclude+=1#counts the times 'Exclude' is recorded
        tuple_exc=Pass,defer,fail #store the credits related to the progression outcome in a tuple
        list_exc.append(tuple_exc)# creates  a nested list containing all values entered relevent to progression outcome
        credit_type=f"Exclude - {Pass},{defer},{fail}"
        ptfour_dict.update({student_id:credit_type})
        print("Exclude")

def dictionary():
    global ptfour_dict
    print("\nPart 4:\n")
    for k,v in ptfour_dict.items():
        print(k," : ",v)

def menu():
    import operations
    while True:
        print("""\nPlease choose your preference\n
             Enter 1 for Histogram
             Enter 2 for List
             Enter 3 for Textfile
             Enter 4 for Dictionary
             Enter 0 to exit """)
        choice=(input(">>>"))
        if choice=="1":
            operations.histogram(Progress,mod_trailer,mod_retriever,Exclude,i)
            print("\nWould you like to explore other options?")
            continue
        elif choice=="2":
            operations.pttwo_list(list_pro,list_trailer,list_retri,list_exc)
            print("\nWould you like to explore other options?")
            continue
        elif choice=="3":
            operations.ptthree_textfile(list_pro,list_trailer,list_retri,list_exc)
            print("\nWould you like to explore other options?")
            continue
        elif choice=="4":
            dictionary()
            print("\nWould you like to explore other options?")
            continue
        elif choice=="0":
            break
        else:
            print("\nPlease enter valid input as instructed in the menu below")
            continue #continues until correct input is given

main()
