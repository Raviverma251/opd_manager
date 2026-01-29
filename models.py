import uuid

class Token:
    def __init__(self, patient_name, p_type):
        self.id = str(uuid.uuid4())[:6]
        self.patient_name = patient_name
        self.type = p_type

        priority_map = {
            'Emergency': 0,
            'Priority': 1,
            'Regular': 2,
            'Walk-in': 3
        }
        self.priority_score = priority_map.get(p_type, 3)

    def __str__(self):
        return f"{self.patient_name} | {self.type} | Priority {self.priority_score}"


class Slot:
    def __init__(self, start_time, end_time, capacity):
        self.slot_id = f"{start_time}-{end_time}"
        self.capacity = capacity
        self.tokens = []

    def is_full(self):
        return len(self.tokens) >= self.capacity

    def add_token(self, token):
        # Case 1: Slot not full
        if not self.is_full():
            self.tokens.append(token)
            self.tokens.sort(key=lambda x: x.priority_score)
            return

        # Case 2: Slot full + Emergency
        if token.type == "Emergency":
            lowest = self.tokens[-1]  # lowest priority patient

            if lowest.priority_score > token.priority_score:
                print(f"⚠️ Emergency override: Removing {lowest.patient_name}")
                self.tokens.pop()
                self.tokens.append(token)
                self.tokens.sort(key=lambda x: x.priority_score)
            else:
                print("❌ Emergency cannot override higher priority patients")
        else:
            print("❌ Slot is full, token cannot be added")

    def show_tokens(self):
        for i, t in enumerate(self.tokens, start=1):
            print(f"{i}. {t}")
