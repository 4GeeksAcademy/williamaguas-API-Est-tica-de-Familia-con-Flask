"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Assign automatic ID
        member["id"] = self._generate_id()

        # Ensure last_name consistency
        member["last_name"] = self.last_name

        # Add member to the list
        self._members.append(member)
        return member

    def delete_member(self, id):
        # Loop through members and delete the one with matching id
        for index, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(index)
                return True
        return False

    def get_member(self, id):
        # Loop through members and return the one with matching id
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
