fever = input("Do you have fever? (yes/no): ")
cough = input("Do you have cough? (yes/no): ")
headache = input("Do you have headache? (yes/no): ")

if fever == "yes" and cough == "yes":
    print("You may have Flu")
elif headache == "yes":
    print("You may have Migraine")
else:
    print("You seem normal")
