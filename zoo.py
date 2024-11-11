class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: 
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 <= age <= 60:
            return 150
        elif age > 60:
            return 100
        elif age < 0:                   #added this line to make sure that if the "age" has assigned any numbers under 0, it'll returning as "Invalid"
            return "Invalid"
