from engine import OPDManager

def run_simulation():
    engine = OPDManager()

    # 1. Setup Doctors and Slots
    engine.add_doctor("Dr. Smith")
    engine.add_slot_to_doctor("Dr. Smith", "09:00", "10:00", capacity=2)
    engine.add_slot_to_doctor("Dr. Smith", "10:00", "11:00", capacity=5)

    # 2. Start Booking
    print(engine.request_token("Dr. Smith", "Rahul", "Regular", "09:00-10:00"))
    print(engine.request_token("Dr. Smith", "Sita", "Regular", "09:00-10:00"))
    
    # Ye fail hona chahiye kyunki capacity 2 hai
    print(engine.request_token("Dr. Smith", "John", "Walk-in", "09:00-10:00")) 

    # Emergency: Ye bypass kar dega
    print("\n--- EMERGENCY ARRIVAL ---")
    print(engine.request_token("Dr. Smith", "Critical Case", "Emergency", "09:00-10:00"))

    # 3. Display Dashboard
    print("\n--- 🏥 LIVE OPD STATUS ---")
    for doc, slots in engine.doctors_data.items():
        print(f"Doctor: {doc}")
        for s in slots:
            p_names = [f"({t.type}){t.patient_name}" for t in s.tokens]
            print(f"  Slot {s.slot_id}: {' -> '.join(p_names)}")

if __name__ == "__main__":
    run_simulation()