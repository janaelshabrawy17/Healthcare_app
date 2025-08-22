import tkinter as tk
from tkinter import messagebox, simpledialog

# ---------------- BACKEND FUNCTIONS (your logic) ----------------

# Example placeholders – paste your real implementations here:
# (I kept short versions, but you can replace them with the full ones you wrote)

users = {}
patients = {}

def create_account():
    name = simpledialog.askstring("Signup", "Enter your name:")
    email = simpledialog.askstring("Signup", "Enter your email:")
    username = simpledialog.askstring("Signup", "Enter username:")
    password = simpledialog.askstring("Signup", "Enter password:", show="*")
    if username in users:
        messagebox.showerror("Error", "Username already exists")
        return False
    users[username] = {"password": password, "name": name, "email": email}
    patients[username] = {}
    messagebox.showinfo("Success", "Account created!")
    return True

def login(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False

def patient_information(username):
    age = simpledialog.askinteger("Patient Info", "Enter Age:")
    cond = simpledialog.askstring("Patient Info", "Conditions (comma separated):")
    patients[username] = {"age": age, "conditions": cond.split(",")}
    messagebox.showinfo("Saved", "Patient info saved!")

def view_patient_information(username):
    if username in patients and patients[username]:
        return str(patients[username])
    return "No information found."

def checker(username):
    return f"Health check for {username}: All vitals normal."

def diet_mode(username):
    info = patients.get(username, {})
    if "diabetes" in ",".join(info.get("conditions", [])).lower():
        return "Low sugar diet"
    return "General healthy diet"

def nearest_doctor(location="giza"):
    return "Dr. Ali in " + location

def reserve_doctor(doctor):
    return f"Reserved {doctor}"

def nearest_hospital(location="giza"):
    return f"Nearest hospital in {location}"

def nearest_pharmacy(location="giza"):
    return f"Nearest pharmacy in {location}"

def reverse_medicine(pharmacy):
    return "Medicines ordered from " + pharmacy

# ---------------- GUI APP ----------------

class HealthcareGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Healthcare System")
        self.root.geometry("600x400")
        self.username = None
        self.show_welcome()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_welcome(self):
        self.clear()
        tk.Label(self.root, text="🏥 Welcome to Healthcare System", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Login", width=20, command=self.show_login).pack(pady=10)
        tk.Button(self.root, text="Create Account", width=20, command=self.show_signup).pack(pady=10)

    def show_login(self):
        self.clear()
        tk.Label(self.root, text="Login", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()
        tk.Label(self.root, text="Password").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def do_login():
            username = username_entry.get()
            password = password_entry.get()
            if login(username, password):
                self.username = username
                messagebox.showinfo("Login", "Login successful")
                self.show_user_menu()
            else:
                messagebox.showerror("Error", "Invalid credentials")

        tk.Button(self.root, text="Login", command=do_login).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_welcome).pack()

    def show_signup(self):
        self.clear()
        tk.Label(self.root, text="Create Account", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Sign Up", command=create_account).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_welcome).pack()

    def show_user_menu(self):
        self.clear()
        tk.Label(self.root, text=f"Welcome {self.username}", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="View Patient Information", width=30,
                  command=lambda: messagebox.showinfo("Info", view_patient_information(self.username))).pack(pady=5)
        tk.Button(self.root, text="Add/Update Information", width=30,
                  command=lambda: patient_information(self.username)).pack(pady=5)
        tk.Button(self.root, text="Diet Mode", width=30,
                  command=lambda: messagebox.showinfo("Diet", diet_mode(self.username))).pack(pady=5)
        tk.Button(self.root, text="Find Nearest Doctor", width=30,
                  command=lambda: messagebox.showinfo("Doctor", reserve_doctor(nearest_doctor()))).pack(pady=5)
        tk.Button(self.root, text="Find Nearest Hospital", width=30,
                  command=lambda: messagebox.showinfo("Hospital", nearest_hospital())).pack(pady=5)
        tk.Button(self.root, text="Find Nearest Pharmacy", width=30,
                  command=lambda: messagebox.showinfo("Pharmacy", nearest_pharmacy())).pack(pady=5)
        tk.Button(self.root, text="Health Check", width=30,
                  command=lambda: messagebox.showinfo("Health", checker(self.username))).pack(pady=5)
        tk.Button(self.root, text="Logout", width=30, command=self.show_welcome).pack(pady=5)


# ---------------- MAIN ----------------

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthcareGUI(root)
    root.mainloop()
