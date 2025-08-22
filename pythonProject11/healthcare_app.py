def nearest_hospital(patient_location, hospitals):
    nearest_hospital = None
    for hospital in hospitals:
        if hospital.get('available', False) and hospital["location"] == patient_location:
            nearest_hospital = hospital
            break
    if nearest_hospital:
        nearest_hospital["available"] = False
        print(f"Hospital in {nearest_hospital['location']} found!")
        return nearest_hospital
    else:
        print("No available hospital found in this location.")
        return None


hospitals = [
    { "location": "giza", 'available': True},
    { "location": "mansoura", 'available': True},
    { "location": "6th october", 'available': True},
    { "location": "maadi", 'available': True},
    { "location": "Helwan", 'available': True},
    { "location": "sohag", 'available': True},
    { "location": "qena", 'available': True},
    { "location": "alexandria", 'available': True}
]

def nearest_pharmacy(patient_location, pharmacies):
    nearest_pharmacy = None
    for pharmacy in pharmacies:
        if pharmacy.get('available', False) and pharmacy["location"] == patient_location:
            nearest_pharmacy = pharmacy
            break
    if nearest_pharmacy:
        print(f"Pharmacy {nearest_pharmacy['location']} found!")
        return nearest_pharmacy
    else:
        print("No available pharmacy found in this location.")
        return None

Pharmacies = [
    { "location": "giza", 'available': True},
    { "location": "Hadek maadi", 'available': True},
    { "location": "6th october", 'available': True},
    { "location": "maadi", 'available': True},
    { "location": "Helwan", 'available': True},
    { "location": "sohag", 'available': True},
    { "location": "qena", 'available': True},
    { "location": "Al_haram", 'available': True}
]


def reverse_medicine(pharmacy):
    medicines = input("Enter your medicines separated by space: ").split()
    confirm = 0

    print("Please confirm your order:\n")

    while confirm == 0:
        for j in range(1, len(medicines) + 1):
            print(f"{j}. {medicines[j - 1]}")

        print("\nPlease confirm your order.")
        print("To confirm, enter 1.")
        print("To edit, enter 2.")
        print("To cancel, enter 0.")

        option = int(input("Enter your choice: "))

        if option == 1:
            print("The order will be delivered to your location.")
            confirm = 1
        elif option == 2:
            print("You can edit your order now.")
            medicines = input("Enter the new list of medicines separated by space: ").split()
        elif option == 0:
            print("Order has been canceled.")
            return


def create_account():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    confirm_password = input('Confirm your password: ')

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return False

    try:
        file = open("users.txt", "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            user_data = line.strip().split("|")
            if user_data[0] == username:
                print("Username already exists. Try a different one.")
                return False
    except FileNotFoundError:
        pass

    file = open("users.txt", "a")
    file.write(username + "|" + password + "|" + name + "|" + email + "\n")
    file.close()

    print("Account created successfully!")
    patient_information(username)
    return True

def patient_information(username):
    patient_file = open(f"{username}_patient_info.txt", "w")
    patient_name = input("Enter the patient's name: ")
    patient_age = input("Enter the patient's age: ")
    patient_gender = input("Enter the patient's gender: ")
    patient_id = input("Enter the patient's ID: ")
    patient_contact_number = input("Enter the patient's phone number: ")
    patient_address = input("Enter the patient's address: ")
    patient_height = input("Enter the patient's height (in CM): ")
    patient_weight = input("Enter the patient's weight (in kilograms): ")
    patient_medical_problems = input("Enter the patient's medical problems: ")

    patient_file.write(f"Name: {patient_name}\n")
    patient_file.write(f"Age: {patient_age}\n")
    patient_file.write(f"Gender: {patient_gender}\n")
    patient_file.write(f"ID: {patient_id}\n")
    patient_file.write(f"Contact Number: {patient_contact_number}\n")
    patient_file.write(f"Address: {patient_address}\n")
    patient_file.write(f"Height: {patient_height}\n")
    patient_file.write(f"Weight: {patient_weight}\n")
    patient_file.write(f"Medical Problems: {patient_medical_problems}\n")

    patient_file.close()
    print(f"Patient information saved in {username}_patient_info.txt")

def view_patient_information(username):
    try:
        patient_file = open(f"{username}_patient_info.txt", "r")
        print("\nPatient Information:")
        print(patient_file.read())
        patient_file.close()
    except FileNotFoundError:
        print("No patient information found. Please add patient information.")

def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    try:
        file = open("users.txt", "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            user_data = line.strip().split("|")
            if username =="admin" and password =="admin":
                admin_menu()
            elif user_data[0] == username and user_data[1] == password:
                print("Login successful!")
                menu(username)
                return True
    except FileNotFoundError:
        print("No accounts found. Please create an account first.")

    print("Invalid username or password.")
    return False

def load_patient_information(username):
    patient_information = {}
    try:
        file = open(f"{username}_patient_info.txt", "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            key, value = line.strip().split(":")
            patient_information[key.strip()] = value.strip()
    except FileNotFoundError:
        print("Patient information file not found.")
    return patient_information

def diet_mode(patient_information):
    if "Weight" in patient_information and "Height" in patient_information:
        weight = float(patient_information["Weight"])
        height = float(patient_information["Height"])
        BMI = weight / ((height / 100) ** 2)
        print(f"BMI: {BMI:.2f}")
        if "diabetes" in patient_information.get("Medical Problems", "").lower():
            if BMI <= 18.5:
                print("Underweight and diabetes, Please follow a balanced diet plan.")
                return "diabetes_gain"
            elif 18.5 < BMI <= 24.9:
                print("Normal weight and diabetes, Please follow a balanced diet plan.")
                return "maintain"
            elif 24.9 < BMI <= 29.9:
                print("Overweight and diabetes, Please follow a balanced diet plan.")
                return "diabetes_lose"
            elif BMI > 30:
                print("Obese and diabetes, Please follow a balanced diet plan.")
                return "diabetes_lose"

        elif "hypertension" in patient_information.get("Medical Problems", "").lower():
            if BMI <= 18.5:
                print("Underweight and hypertension, Please follow a balanced diet plan for weight gain.")
                return "hypertention_gain"
            elif 18.5 < BMI <= 24.9:
                print("Normal weight and hypertension, Please follow a balanced diet plan.")
                return "maintain"
            elif 24.9 < BMI <= 29.9:
                print("Overweight and hypertension, Please follow a balanced diet plan.")
                return "hypertention_lose"
            elif BMI > 30:
                print("Obese and hypertension, Please follow a balanced diet plan.")
                return "hypertention_lose"

        if BMI <= 18.5:
            print("Underweight. Please follow a diet plan to gain weight.")
            return "gain"
        elif 18.5 < BMI <= 24.9:
            print("Normal weight. Maintain your current weight.")
            return "maintain"
        elif 24.9 < BMI <= 29.9:
            print("Overweight. Please follow a diet plan to lose weight.")
            return "lose"
        else:
            print("Strict diet plan.")
            return "strict"
    else:
        print("Height or weight information is missing.")
        return None

def weight_loss_plan():
    return [{"food": "Breakfast: Plain Greek yogurt with strawberries and low-sugar granola."},
            {"food": "Lunch: Tuna melt sandwich with cheese and tomatoes on whole grain bread."},
            {"food": "Dinner: Chicken with brown rice and stir-fried vegetables."}]

def weight_gain_plan():
    return [{"food": "Breakfast: Peach-Mango Smoothie Bowl and 1 hard-boiled egg."},
            {"food": "Lunch: Vegetable & Tuna Pasta Salad with mango juice."},
            {"food": "Dinner: Creamy Chicken & Mushroom One-Pot Pasta."}]

def keep_weight_plan():
    return [{"food": "Breakfast: Scrambled eggs, whole grain toast, and tomato."},
            {"food": "Lunch: Chicken Caesar salad with cucumbers, lettuce, and vinaigrette."},
            {"food": "Dinner: Grilled salmon with spinach and quinoa."}]

def strict_plan():
    return [{"food": "Breakfast: Oatmeal with almond butter."},
            {"food": "Lunch: Grilled chicken with leafy greens."},
            {"food": "Dinner: Grilled fish with vegetables."}]
def diabetes_lose_plan():
    return [{"food": "Breakfast: Whole-wheat bread, a piece of fruit, and coffee."},
            {"food": "Lunch: Roast beef sandwich on wheat bread with lettuce, tomato, and mayonnaise."},
            {"food": "Dinner: Salmon with baked potato, carrots, and green beans."}]

def diabetes_gain_plan():
    return [{"food": "Breakfast: 1 cup low-fat plain Greek yogurt, ¼ cup blueberries, and 3 Tbsp. chopped walnuts."},
            {"food": "Lunch: White Bean & Veggie Salad."},
            {"food": "Dinner: Stuffed Potatoes with Salsa & Beans, mixed greens."}]

def hypertention_gain_plan():
    return [{"food": "Breakfast: 1 cup of oatmeal without salt, 1 medium banana, and 1 cup fat-free milk."},
            {"food": "Lunch: White Bean & Veggie Salad."},
            {"food": "Dinner: Vegetarian pasta with marinara sauce and summer squash."}]

def hypertention_lose_plan():
    return [{"food": "Breakfast: Avocado toast, 1 poached egg, 1 slice whole-wheat toast."},
            {"food": "Lunch: Tuna salad on crackers with low-sodium canned tuna, diced onion, and bell pepper."},
            {"food": "Dinner: Vegetable stir-fry with sesame oil, onion, bell pepper, and mushrooms."}]
def choose_diet(goal):
    if goal == "lose":
        return weight_loss_plan()
    elif goal == "gain":
        return weight_gain_plan()
    elif goal == "maintain":
        return keep_weight_plan()
    elif goal == "diabetes_lose":
        return diabetes_lose_plan()
    elif goal == "diabetes_gain":
        return diabetes_gain_plan()
    elif goal == "hypertention_lose":
        return hypertention_lose_plan()
    elif goal == "hypertention_gain":
        return hypertention_gain_plan()
    else:
        return strict_plan()
def nearest_doctor(patient_location, doctors):
    nearest_doctor = None
    for doctor in doctors:
        if doctor.get('available', False) and doctor["location"] == patient_location:
            nearest_doctor = doctor
            break
    if nearest_doctor:
        print(f"Doctor {nearest_doctor['name']} found!")
        return nearest_doctor
    else:
        print("No available doctors found in this location.")
        return None
def reserve_doctor(doctor):
    if doctor:
        confirm = input(f"Do you want to reserve Dr. {doctor['name']} (Specialty: {doctor['specialty']})? (yes/no): ").lower()
        if confirm == "yes":
            doctor["available"] = False
            print(f"Doctor {doctor['name']} has been reserved successfully!")
            return doctor
        else:
            print("Reservation cancelled.")
            return None
    else:
        print("No doctor to reserve.")
        return None


doctors = [
    {"name": "Dr.Aliaa", "specialty": "Cardiologist", "location": "giza", 'available': True},
    {"name": "Dr.Mohamed", "specialty": "Obstetrics and Gynecology", "location": "mansoura", 'available': True},
    {"name": "Dr.howayda", "specialty": "Internal medicine", "location": "6th october", 'available': True},
    {"name": "Dr.omar", "specialty": "Chondrodysplasia", "location": "maady", 'available': True},
    {"name": "Dr.jana", "specialty": "Dermatology", "location": "sohag", 'available': True},
    {"name": "Dr.sama", "specialty": "Neurology", "location": "assuit", 'available': True},
    {"name": "Dr.radwa", "specialty": "Pediatrics", "location": "qena", 'available': True},
    {"name": "Dr.basmala", "specialty": "Ophthalmology", "location": "alexandria", 'available': True}
]
def admin_menu():
    while True:
        print("\nMenu:")
        print("1. View Patient Information")
        print("2. Add Patient Information")
        print("3. Log out")
        choice = input("Enter your choice: ")

        if choice == "1":
            username=input("enter username of patient that you want to view")
            view_patient_information(username)
        elif choice == "2":
            username=input("enter username of patient that you want to add")
            print("Please Know that you will enter the histoy of patiant from beganing ")

            patient_information(username)
        else:
            exit()
def menu(username):
    while True:
        print("\nMenu:")
        print("1. View Patient Information")
        print("2. Checker")
        print("3. Diet Mode")
        print("4. Find Nearest Doctor")
        print("5. Nearest")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_patient_information(username)
        elif choice == "2":
            checker(username)
        elif choice == "3":
            patient_info = load_patient_information(username)
            goal = diet_mode(patient_info)
            if goal:
                diet_plan = choose_diet(goal)
                print("Diet Plan:")
                for meal in diet_plan:
                    print(f"- {meal['food']}")
        elif choice == "4":
            patient_location = load_patient_information(username).get("Address")

            reserve_doctor(nearest_doctor(patient_location, doctors))

        elif choice == "6":
            print("Logged out successfully!")
            return

        elif choice=="5":

            action = input("Type 'pharmacy' for nearest pharmacy, 'hospital' for nearest hospital, or 'exit' to exit: ").lower()
            if action == "pharmacy":
                nearest_pharmacy_info = nearest_pharmacy("giza", Pharmacies)
                if nearest_pharmacy_info:
                    reverse_medicine(nearest_pharmacy_info)
            elif action == "hospital":
                nearest_hospital_info = nearest_hospital("giza", hospitals)
            elif action == "exit":
                print("Exiting the system.")

    menu(username)


def add_remove_medical_information(username):
    if username != "admin":
        print("You need to be an admin to modify medical information.")
        return

    print("Admin access granted. You can now modify patient medical information.")
    patient_username = input("Enter the patient's username that you want to modify: ")
    find_patient_file = f"{patient_username}_patient_info.txt"

    try:
        with open(find_patient_file, "r") as patient_file:
            lines = patient_file.readlines()

        patient_information = {}
        for line in lines:
            key, value = line.strip().split(":")
            patient_information[key.strip()] = value.strip()

        print("Current medical information:")
        for key, value in patient_information.items():
            print(f"{key}: {value}")
        while True:
            action = input("Do you want to add or remove medical information? (add/remove/exit): ").lower()

            if action == "add":
                medical_field = input("Enter the medical field you want to add : ")
                new_value = input(f"Enter the new value for {medical_field}: ")
                patient_information[medical_field] = new_value
                print(f"{medical_field} added/updated successfully.")

            elif action == "remove":
                medical_field = input("Enter the medical field you want to remove : ")
                if medical_field in patient_information:
                    del patient_information[medical_field]
                    print(f"{medical_field} removed successfully.")
                else:
                    print(f"{medical_field} does not exist in the patient's records.")

            elif action == "exit":
                break
            else:
                print("Invalid action. Please choose 'add', 'remove', or 'exit'.")

        with open(find_patient_file, "w") as patient_file:
            for key, value in patient_information.items():
                patient_file.write(f"{key}: {value}\n")

        print("Patient medical information updated successfully.")

    except FileNotFoundError:
        print(f"Patient file for {patient_username} not found.")


def write_to_history(username, entry):
    filename = f"{username}_history.txt"
    file = open(filename, 'a')
    file.write(entry + "\n")
    file.close()


def get_blood_pressure():
    systolic = int(input("Enter your systolic pressure (mmHg): "))
    diastolic = int(input("Enter your diastolic pressure (mmHg): "))
    if systolic < 90 or diastolic < 60:
        print(f"Systolic: {systolic} mmHg, Diastolic: {diastolic} mmHg - Low blood pressure detected.")
        return f"Systolic: {systolic} mmHg, Diastolic: {diastolic} mmHg - Low blood pressure detected."
    elif systolic > 140 or diastolic > 90:
        print(f"Systolic: {systolic} mmHg, Diastolic: {diastolic} mmHg - High blood pressure detected.")
        return f"Systolic: {systolic} mmHg, Diastolic: {diastolic} mmHg - High blood pressure detected."
    else:
        print(f"Systolic: {systolic} mmHg, Diastolic: {diastolic} mmHg - Blood pressure is normal.")
        return f"Systolic: {systolic} mmHg, Diastolic: {diastolic} mmHg - Blood pressure is normal."


def get_blood_glucose():
    glucose = float(input("Enter your blood glucose level (mg/dL): "))
    if glucose < 70:
        print(f"Blood Glucose: {glucose} mg/dL - Hypoglycemia (Low blood sugar) detected.")
        return f"Blood Glucose: {glucose} mg/dL - Hypoglycemia (Low blood sugar) detected."
    elif glucose > 180:
        print(f"Blood Glucose: {glucose} mg/dL - Hyperglycemia (High blood sugar) detected.")
        return f"Blood Glucose: {glucose} mg/dL - Hyperglycemia (High blood sugar) detected."
    else:
        print(f"Blood Glucose: {glucose} mg/dL - Blood glucose level is normal.")
        return f"Blood Glucose: {glucose} mg/dL - Blood glucose level is normal."


def get_heart_rate():
    heart_rate = int(input("Enter your heart rate (beats per minute): "))
    if heart_rate < 60:
        print(f"Heart Rate: {heart_rate} bpm - Low heart rate detected (bradycardia).")
        return f"Heart Rate: {heart_rate} bpm - Low heart rate detected (bradycardia)."
    elif heart_rate > 100:
        print(f"Heart Rate: {heart_rate} bpm - High heart rate detected (tachycardia).")
        return f"Heart Rate: {heart_rate} bpm - High heart rate detected (tachycardia)."
    else:
        print( f"Heart Rate: {heart_rate} bpm - Heart rate is normal.")
        return f"Heart Rate: {heart_rate} bpm - Heart rate is normal."


def get_temperature():
    temperature = float(input("Enter your body temperature (°C): "))
    if temperature < 36.1:
        print(f"Temperature: {temperature} °C - Low body temperature detected.")
        return f"Temperature: {temperature} °C - Low body temperature detected."
    elif temperature > 37.5:
        print(f"Temperature: {temperature} °C - High body temperature detected.")
        return f"Temperature: {temperature} °C - High body temperature detected."
    else:
        print (f"Temperature: {temperature} °C - Body temperature is normal.")
        return f"Temperature: {temperature} °C - Body temperature is normal."


def get_spo2():
    spo2 = float(input("Enter your SpO2 level (%): "))
    if spo2 < 90:
        print(f"SpO2: {spo2}% - Low oxygen saturation detected.")
        return f"SpO2: {spo2}% - Low oxygen saturation detected."
    elif spo2 > 100:
        print(f"SpO2: {spo2}% - Invalid SpO2 value. The maximum is 100%.")
        return f"SpO2: {spo2}% - Invalid SpO2 value. The maximum is 100%."
    else:
        print(f"SpO2: {spo2}% - Oxygen saturation is normal.")
        return f"SpO2: {spo2}% - Oxygen saturation is normal."


def health_check(username, option):
    if option == 1:
        return get_blood_pressure()
    elif option == 2:
        return get_blood_glucose()
    elif option == 3:
        return get_heart_rate()
    elif option == 4:
        return get_temperature()
    elif option == 5:
        return get_spo2()
    else:
        return "Invalid option."


def checker(username):
    print(f"Hello, {username}! Please choose a health check option:")
    print("1. Blood Pressure")
    print("2. Blood Glucose")
    print("3. Heart Rate")
    print("4. Temperature")
    print("5. SpO2")

    option = int(input("Enter the number of the option you want to check (1-5): "))

    result = health_check(username, option)

    if result == "Invalid option.":
        print(result)
        return

    history_entry = f"Health Check for {username} - Option {option}:\n{result}\n"
    write_to_history(username, history_entry)

    another_check = input("Would you like to perform another health check? (yes/no): ").lower()
    if another_check == "yes":
        checker(username)



def main():
    try:
        open("users.txt", "x").close()
    except FileExistsError:
        pass

    print("Welcome!")
    choice = input("Do you already have an account? (yes/no): ").lower()

    if choice == "yes":
        if not login():
            print("Login failed. Please try again.")
    elif choice == "no":
        if create_account():
            print("Account created successfully. Please log in to access the menu.")
            login()
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
