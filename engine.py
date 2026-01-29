from models import Token, Slot

class OPDManager:
    def __init__(self):
        self.doctors_data = {}

    def add_doctor(self, doctor_name):
        if doctor_name not in self.doctors_data:
            self.doctors_data[doctor_name] = []

    def add_slot_to_doctor(self, doctor_name, start_time, end_time, capacity):
        if doctor_name not in self.doctors_data:
            return "❌ Doctor not found!"
        self.doctors_data[doctor_name].append(Slot(start_time, end_time, capacity))

    def request_token(self, doctor_name, patient_name, p_type, preferred_slot_id):
        if doctor_name not in self.doctors_data:
            return "❌ Doctor not found!"

        target_slot = next(
            (s for s in self.doctors_data[doctor_name] if s.slot_id == preferred_slot_id),
            None
        )

        if not target_slot:
            return "❌ Slot not found!"

        new_token = Token(patient_name, p_type)
        result = target_slot.add_token(new_token)
        return f"✅ Token {new_token.id} issued for {patient_name}"

    def cancel_token(self, doctor_name, slot_id, token_id):
        if doctor_name not in self.doctors_data:
            return "❌ Doctor not found!"

        target_slot = next(
            (s for s in self.doctors_data[doctor_name] if s.slot_id == slot_id),
            None
        )

        if not target_slot:
            return "❌ Slot not found!"

        before = len(target_slot.tokens)
        target_slot.tokens = [t for t in target_slot.tokens if t.id != token_id]

        if len(target_slot.tokens) < before:
            return f"⚠️ Token {token_id} cancelled."
        return "❌ Token not found."
