# MedBot: Simple Medical Chatbot

# Step 1: Greeting
print("Hello! I am MedBot, your medical helper.")

# Step 2: Collect basic info
name = input("What is your name? ")
age = input("How old are you? ")
sex = input("What is your sex (M/F)? ")

# Step 3: Ask about symptoms
symptom = input("What symptoms are you experiencing? ")

# Step 4: Basic advice
if "fever" in symptom.lower():
    print("You have a fever. Make sure to rest and drink lots of water.")
elif "chest pain" in symptom.lower():
    print("Chest pain can be serious. Please see a doctor immediately!")
else:
    print("Monitor your symptoms and see a doctor if things get worse.")

# Step 5: End
print("Thank you for using MedBot. Take care!")
