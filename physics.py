# PHYSICS CALCULATOR

# 1. VELOCITY
def velocity():
    print("\n--- VELOCITY ---")

    distance = float(input("Enter distance: "))
    time = float(input("Enter time: "))

    if time == 0:
        print("Time cannot be zero.")
    else:
        v = distance / time
        print("Velocity =", v, "m/s")


# 2. FORCE
def force():
    print("\n--- FORCE ---")

    mass = float(input("Enter mass: "))
    acceleration = float(input("Enter acceleration: "))

    F = mass * acceleration
    print("Force =", F, "N")


# 3. WORK DONE
def work_done():
    print("\n--- WORK DONE ---")

    force_value = float(input("Enter force: "))
    distance = float(input("Enter distance: "))

    W = force_value * distance
    print("Work Done =", W, "J")


# 4. KINETIC ENERGY
def kinetic_energy():
    print("\n--- KINETIC ENERGY ---")

    mass = float(input("Enter mass: "))
    velocity = float(input("Enter velocity: "))

    KE = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", KE, "J")


# 5. DENSITY
def density():
    print("\n--- DENSITY ---")

    mass = float(input("Enter mass: "))
    volume = float(input("Enter volume: "))

    if volume == 0:
        print("Volume cannot be zero.")
    else:
        D = mass / volume
        print("Density =", D, "kg/m³")


# MAIN PROGRAM

while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Velocity")
    print("2. Force")
    print("3. Work Done")
    print("4. Kinetic Energy")
    print("5. Density")

    choice = input("\nChoose an operation (1-5): ")

    if choice == "1":
        velocity()

    elif choice == "2":
        force()

    elif choice == "3":
        work_done()

    elif choice == "4":
        kinetic_energy()

    elif choice == "5":
        density()

    else:
        print("Invalid choice. Select 1-5.")

    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using the Physics Calculator!")
        break