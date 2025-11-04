# abstraction is when i hide the complex details for something a lot more simple.

# personal info
# a fuction allows us to wrap data into a box for reuse
def personalInformation():
    question1 = input("How old are you?")
    question2 = input("where do you live?")
    question3 = input("what school do you go to?")
    print(question1 + question2 + question3)

personalInformation()
personalInformation()
personalInformation()

def age():
    q1 = int(input("when were you born"))
    q2 = int(input("what year is it now?"))
    answer = q1 +q2
    result = print(f"You are {answer} years old")

age()
age()
age()