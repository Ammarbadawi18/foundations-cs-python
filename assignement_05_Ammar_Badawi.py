###############Family Tree################
class FamilyMember:
    def __init__(self, name, familyName, birthdate):
        self.name = name
        self.familyName = familyName
        self.birthdate = birthdate
        self.children = []

def addFamilyMember(familyTree):
    name = input("Enter member's name: ")
    familyName = input("Enter member's family name: ")
    birthdate = input("Enter member's birthdate (YYYY-MM-DD): ")
    parentName = input("Enter parent's name (or enter 'root' if this is a root member): ")
    if parentName.lower() == 'root':
        familyTree[name] = FamilyMember(name, familyName, birthdate)
    else:
        parentMember = familyTree.get(parentName)
        if parentMember:
            childMember = FamilyMember(name, familyName, birthdate)
            parentMember.children.append(childMember)
            familyTree[name] = childMember
            print(f"{name} {familyName} added to the family tree under {parentName}")
        else:
            print(f"Parent with name {parentName} not found.")

def displaySortedBirthdays(familyTree):
    def sortByBirthdate(member):
        return member.birthdate
    sortedMembers = sorted(familyTree.values(), key=sortByBirthdate)
    for member in sortedMembers:
        print(f"{member.name}: {member.birthdate}")

def findRelationship(familyTree):
    person1 = input("Enter the name of the first person: ")
    person2 = input("Enter the name of the second person: ")
    member1 = familyTree.get(person1)
    member2 = familyTree.get(person2)
    if member1 and member2:
        relationship = "sibling" if member1 in member2.children or member2 in member1.children else "non-sibling"
        print(f"The relationship between {person1} and {person2} is: {relationship}")
    else:
        print("One or both persons not found in the family tree.")

def countSameFirstNames(familyTree):
    firstName = input("Enter the first name to count: ").lower()
    count = 0
    for member in familyTree.values():
        if member.name.lower().startswith(firstName):
            count += 1
    print(f"The count of family members with the first name {firstName} is: {count}")

familyTree = {}
while True:
    print("- - - - - - - - - - - - - - -\n1. Add Family Member\n2. Display Sorted Birthdays\n3. Find Relationship\n4. Count first names \n5. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        addFamilyMember(familyTree)
    elif choice == 2:
        displaySortedBirthdays(familyTree)
    elif choice == 3:
        findRelationship(familyTree)
    elif choice == 4:
        countSameFirstNames(familyTree)
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
####################################################

########################SocialMediaPlatform########################

class SocialMediaPlatform:
  def __init__(self):
      self.users = {}
      self.edges = {}

  def addUser(self, username):
      if username in self.users:
          print("User already exists. Please choose another username.")
      else:
          self.users[username] = True
          self.edges[username] = []

  def removeUser(self, username):
      if username in self.users:
          del self.users[username]
          del self.edges[username]
          for user, friendships in self.edges.items():
              if username in friendships:
                  friendships.remove(username)
      else:
          print("User not found. Please make sure of the username.")

  def sendFriendRequest(self, user1, user2):
      if user1 in self.users and user2 in self.users:
          self.edges[user1].append(user2)
          self.edges[user2].append(user1)
          print(f"Friend request sent from {user1} to {user2}.")
      else:
          print("Invalid usernames. Please make sure both users exist.")

  def removeFriend(self, user1, user2):
      if user1 in self.users and user2 in self.users:
          if user2 in self.edges[user1] and user1 in self.edges[user2]:
              self.edges[user1].remove(user2)
              self.edges[user2].remove(user1)
              print(f"{user1} and {user2} are no longer friends.")
          else:
              print(f"{user1} and {user2} are not friends.")
      else:
          print("Invalid usernames. Please make sure both users exist.")

  def viewFriends(self, username):
      if username in self.users:
          friends = self.edges[username]
          print(f"{username}'s friends: {', '.join(friends)}")
      else:
          print("User not found. Please make sure of the username.")

  def viewAllUsers(self):
      print("All users on the platform:")
      for username in self.users:
          print(username)

  def displayMenu(self):
      while True:
          print("\n1. Add a user")
          print("2. Remove a user")
          print("3. Send a friend request")
          print("4. Remove a friend")
          print("5. View your list of friends")
          print("6. View the list of users on the platform")
          print("7. Exit")

          choice = input("Enter a choice: ")

          if choice == '1':
              username = input("Enter a username: ")
              self.addUser(username)
          elif choice == '2':
              username = input("Enter the username to remove: ")
              self.removeUser(username)
          elif choice == '3':
              user1 = input("Enter your username: ")
              user2 = input("Enter the username of the friend: ")
              self.sendFriendRequest(user1, user2)
          elif choice == '4':
              user1 = input("Enter your username: ")
              user2 = input("Enter the username of the friend to remove: ")
              self.removeFriend(user1, user2)
          elif choice == '5':
              username = input("Enter your username: ")
              self.viewFriends(username)
          elif choice == '6':
              self.viewAllUsers()
          elif choice == '7':
              print("Exiting the program. Goodbye")
              break
          else:
              print("Please enter a valid option.")

if __name__ == "__main__":
  platform = SocialMediaPlatform()
  platform.displayMenu()




