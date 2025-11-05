# Vehicle Fault Diagnosis Expert System 🚗


def get_yes_no(question):
    """Ask a yes/no question and return True or False."""
    ans = input(question + " (yes/no): ").strip().lower()
    return ans == "yes"

def diagnose_vehicle():
    print("=======================================")
    print("     Vehicle Fault Diagnosis System     ")
    print("=======================================\n")

    engine_wont_start = get_yes_no("Does the engine fail to start?")
    noise_from_engine = get_yes_no("Do you hear unusual engine noises?")
    smoke_from_exhaust = get_yes_no("Is there smoke coming from the exhaust?")
    oil_leak = get_yes_no("Is there any oil leaking from the vehicle?")
    overheating = get_yes_no("Is the engine overheatinong?")
    low_mileage = get_yes_no("Are you getting low fuel mileage?")
    vibration = get_yes_no("Do you feel vibration while driving?")
    warning_light = get_yes_no("Is the check-engine light ON?")


    if engine_wont_start and warning_light:
        print("\n⚠️ Possible Issue: Battery or Starter Motor Failure")
    elif engine_wont_start and not warning_light:
        print("\n⚠️ Possible Issue: Fuel System Problem or Empty Tank")
    elif smoke_from_exhaust and overheating:
        print("\n⚠️ Possible Issue: Head Gasket Leak or Coolant Problem")
    elif oil_leak and smoke_from_exhaust:
        print("\n⚠️ Possible Issue: Engine Oil Leakage into Combustion Chamber")
    elif low_mileage and warning_light:
        print("\n⚠️ Possible Issue: Faulty Oxygen Sensor or Air Filter Blockage")
    elif vibration and noise_from_engine:
        print("\n⚠️ Possible Issue: Engine Mounts or Transmission Problem")
    elif overheating and not smoke_from_exhaust:
        print("\n⚠️ Possible Issue: Radiator or Coolant Leak")
    elif noise_from_engine and not vibration:
        print("\n⚠️ Possible Issue: Worn-out Timing Belt or Low Engine Oil")
    else:
        print("\n✅ No major issue detected. Regular servicing recommended.")

    print("\n=======================================")
    print("Thank you for using the Expert System!")
    print("=======================================")



if __name__ == "__main__":
    diagnose_vehicle()
    
