#
# DSAContactHashTable.py
#

from DSAContact import DSAContact

class DSAContactHashTable:
    def __init__(self, size=10):
        # Initialize the hash table with a specified size
        self.size = size
        # Create a list to hold the hash table, initialized with None values
        self.table = [None] * self.size

    def _hash(self, phone_number):
        # Hash function to calculate the index for a given phone number
        return hash(phone_number) % self.size

    def add_contact(self, contact):
        # Calculate the index using the hash function
        index = self._hash(contact.phone_number)
        # Check if the index is empty
        if self.table[index] is None:
            # If empty, store the contact at the index
            self.table[index] = contact
        else:
            # Handle collision by chaining
            if isinstance(self.table[index], list):
                # If collision occurs and the index already contains a list, append the contact to the list
                self.table[index].append(contact)
            else:
                # If collision occurs and the index contains a single contact, convert it to a list and append the new contact
                self.table[index] = [self.table[index], contact]

    def delete_contact(self, phone_number):
    # Calculate the index using the hash function
        index = self._hash(phone_number)
    # Check if the index is not empty
        if self.table[index] is not None:
            # If the index contains a list of contacts
            if isinstance(self.table[index], list):
                # Iterate through the list of contacts at the index
                for i, contact in enumerate(self.table[index]):
                    # Check if the phone number matches
                    if contact.phone_number == phone_number:
                        # If found, delete the contact from the list
                        del self.table[index][i]
                        print("Contact deleted successfully.")
                        return
                # If the contact was not found in the list
                print("Contact not found.")
            # If the index contains a single contact
            elif self.table[index].phone_number == phone_number:
                # Delete the contact at the index
                self.table[index] = None
                print("Contact deleted successfully.")
            else:
                # If the contact was not found at the index
                print("Contact not found.")
        else:
            # If the index is empty
            print("Contact not found.")


    def update_contact(self, phone_number, updated_contact):
        # Calculate the index using the hash function
        index = self._hash(phone_number)
        # Check if the index is not empty
        if self.table[index] is not None:
            # If the index contains a list of contacts
            if isinstance(self.table[index], list):
                # Iterate through the list of contacts at the index
                for i, contact in enumerate(self.table[index]):
                    # Check if the phone number matches
                    if contact.phone_number == phone_number:
                        # Update the contact with the provided updated_contact
                        self.table[index][i] = updated_contact
                        print("Contact updated successfully.")
                        return
                # If the contact was not found in the list
                print("Contact not found.")
            # If the index contains a single contact
            elif self.table[index].phone_number == phone_number:
                # Update the contact at the index with the provided updated_contact
                self.table[index] = updated_contact
                print("Contact updated successfully.")
            else:
                # If the contact was not found at the index
                print("Contact not found.")
        else:
            # If the index is empty
            print("Contact not found.")


    def display_contacts(self):
        # Iterate through each item in the hash table
        for item in self.table:
            # Check if the item is not None (i.e., there is a contact at this index)
            if item is not None:
                # If the item is a list (collision handling)
                if isinstance(item, list):
                    # Iterate through each contact in the list and print its details
                    for contact in item:
                        print(contact)
                else:
                    # If the item is a single contact, print its details
                    print(item)

    def search_contacts(self, search_term):
        found_contacts = []  # List to store found contacts
        # Iterate through each item in the hash table
        for item in self.table:
            # Check if the item is not None (i.e., there is a contact at this index)
            if item is not None:
                # If the item is a list (collision handling)
                if isinstance(item, list):
                    # Iterate through each contact in the list
                    for contact in item:
                        # Check if the search term matches the contact's name or phone number
                        if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                            # If a match is found, add the contact to the found_contacts list
                            found_contacts.append(contact)
                else:
                    # If the item is a single contact
                    # Check if the search term matches the contact's name or phone number
                    if search_term.lower() in item.name.lower() or search_term in item.phone_number:
                        # If a match is found, add the contact to the found_contacts list
                        found_contacts.append(item)
        # Check if any contacts were found
        if found_contacts:
            print("Matching contacts found:")
            # Iterate through the found contacts and print their details
            for contact in found_contacts:
                print(contact)
        else:
            # If no contacts were found, print a message
            print("No matching contacts found.")


    def get_contact_names(self):
        contact_names = []  # List to store contact names
        # Iterate through each item in the hash table
        for item in self.table:
            # Check if the item is not None (i.e., there is a contact at this index)
            if item is not None:
                # If the item is a list (collision handling)
                if isinstance(item, list):
                    # Iterate through each contact in the list and append its name to contact_names
                    for contact in item:
                        contact_names.append(contact.name)
                else:
                    # If the item is a single contact, append its name to contact_names
                    contact_names.append(item.name)
        return contact_names  # Return the list of contact names

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr  # Base case: return the array if it has one element or is empty
        mid = len(arr) // 2  # Calculate the midpoint of the array
        left_half = arr[:mid]  # Split the array into left half
        right_half = arr[mid:]  # Split the array into right half
        # Recursively call merge_sort on left and right halves
        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)
        return self.merge(left_half, right_half)  # Merge the sorted left and right halves

    def merge(self, left, right):
        result = []  # List to store the merged result
        left_index, right_index = 0, 0  # Initialize indices for the left and right subarrays
        # Iterate while both left and right indices are within their respective subarrays
        while left_index < len(left) and right_index < len(right):
            # Compare the elements at the current left and right indices
            if left[left_index] < right[right_index]:
                # If the element in the left subarray is smaller, append it to the result and move the left index
                result.append(left[left_index])
                left_index += 1
            else:
                # If the element in the right subarray is smaller, append it to the result and move the right index
                result.append(right[right_index])
                right_index += 1
        # Append the remaining elements from the left and right subarrays (if any) to the result
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result  # Return the merged result

    def sort_contacts_by_name(self):
        contact_names = self.get_contact_names()  # Get the names of all contacts
        sorted_names = self.merge_sort(contact_names)  # Sort the contact names using merge sort
        sorted_contacts = []  # List to store sorted contacts
        # Iterate through each sorted name
        for name in sorted_names:
            # Iterate through each item in the hash table
            for item in self.table:
                if item is not None:
                    # If the item is a list (collision handling)
                    if isinstance(item, list):
                        # Iterate through each contact in the list
                        for contact in item:
                            # If the contact's name matches the sorted name, append it to sorted_contacts
                            if contact.name == name:
                                sorted_contacts.append(contact)
                    else:
                        # If the item is a single contact, compare its name with the sorted name
                        if item.name == name:
                            sorted_contacts.append(item)  # Append the contact to sorted_contacts
        return sorted_contacts  # Return the sorted list of contacts by name


    def filter_contacts_by_group(self, group):
        filtered_contacts = []  # List to store contacts belonging to the specified group
        # Iterate through each item in the hash table
        for item in self.table:
            if item is not None:
                # If the item is a list (collision handling)
                if isinstance(item, list):
                    # Iterate through each contact in the list
                    for contact in item:
                        # Check if the contact belongs to the specified group
                        if contact.group == group:
                            # If it does, append the contact to filtered_contacts
                            filtered_contacts.append(contact)
                else:
                    # If the item is a single contact, check if it belongs to the specified group
                    if item.group == group:
                        # If it does, append the contact to filtered_contacts
                        filtered_contacts.append(item)
        return filtered_contacts  # Return the list of contacts belonging to the specified group

# Read contacts from file and store in hash table
def read_contacts(filename):
    # Initialize an empty ContactHashTable object
    contact_table = DSAContactHashTable()
    # Open the specified file in read mode
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into a list of data elements using comma as the delimiter
            data = line.strip().split(',')
            # Check if the split data contains exactly four elements, indicating correct format for contact information
            if len(data) == 4:
                # Extract phone number, name, email, and group from the data list
                phone_number, name, email, group = data
                # Create a DSAContact object with the extracted information
                contact = DSAContact(name, phone_number, email, group)
                # Add the created contact to the contact_table using the add_contact method
                contact_table.add_contact(contact)
    # Return the populated contact_table
    return contact_table

# Example usage:
contact_table = read_contacts('contact_list.txt')
contact_table.display_contacts()
contact_table = DSAContactHashTable()


