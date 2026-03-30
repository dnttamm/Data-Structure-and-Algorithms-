#
# DSAContact.py
#


class DSAContact:
    def __init__(self, name, phone_number, email, group):
        # Initialize contact attributes
        self.name = name  # Name of the contact
        self.phone_number = phone_number  # Phone number of the contact
        self.email = email  # Email address of the contact
        self.group = group  # Group to which the contact belongs (e.g., Family, Workplace, Friends)

    def __str__(self):
        # Return a string representation of the contact
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nGroup: {self.group}\n"