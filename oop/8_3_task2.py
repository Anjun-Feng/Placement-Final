import textwrap
# --- Pack Class ---
class Pack:
    """Represents a pack that can hold items."""
    def __init__(self, size: int):
        self.size = size
        self.contents = [] # A list to hold Item objects

    def _get_current_load(self) -> int:
        """Helper method to calculate the current occupied space."""
        return sum(item.getSize() for item in self.contents)

    def packCapacity(self):
        """Returns a message indicating pack size, current load, and remaining space."""
        current_load = self._get_current_load()
        remaining = self.size - current_load
        return f"Pack Capacity: {current_load}/{self.size} (Space remaining: {remaining})"

    def addItem(self, item: Item):
        """Adds an item to the pack if there is enough space."""
        current_load = self._get_current_load()
        if current_load + item.getSize() <= self.size:
            self.contents.append(item)
            print(f"Success: Added '{item.name}' to the pack.")
        else:
            print(f"Failure: Cannot add '{item.name}'. Not enough space in the pack.")
            
    def dropItem(self, item: Item):
        """Removes a specified item from the pack if it exists."""
        if item in self.contents:
            self.contents.remove(item)
            print(f"Success: Dropped '{item.name}' from the pack.")
        else:
            print(f"Failure: Cannot drop '{item.name}'. It is not in the pack.")

    def __str__(self) -> str:
        """Returns a string representation of the pack and its contents."""
        header = "--- Pack Contents ---"
        capacity_info = self.packCapacity()
        if not self.contents:
            return f"{header}\nThe pack is empty.\n{capacity_info}"
        
        # Use textwrap to format item descriptions neatly
        items_str_list = []
        for item in self.contents:
            # Get the base string from the item's __str__ method
            base_str = str(item)
            # Wrap the description part for better readability
            wrapped_str = textwrap.fill(base_str, width=60, subsequent_indent='    ')
            items_str_list.append(wrapped_str)

        items_str = "\n".join(items_str_list)
        return f"{header}\n{items_str}\n---------------------\n{capacity_info}"
    
# --- Base Item Class ---
class Item:
    """Represents a generic item in the game."""
    def __init__(self, name: str, description: str, size: int):
        self.name = name
        self.description = description
        self.size = size

    def getSize(self) -> int:
        """Returns the size of the item."""
        return self.size

    def __str__(self) -> str:
        """Returns a string representation of the item."""
        return f"- {self.name} (Size: {self.size}): {self.description}"

# --- Item Subclasses ---
class Potion(Item):
    """Represents a potion, inheriting from Item."""
    def __init__(self, name: str, description: str, size: int, potency: int = 10):
        # Initialize the parent Item class
        super().__init__(name, description, size)
        # Set the potion-specific attribute
        self.potency = potency

    def use(self):
        """Generates a message indicating the potion has been used."""
        print(f"You used the '{self.name}'. It feels invigorating!")

    def __str__(self) -> str:
        """Overrides the parent __str__ to include potency."""
        return f"- {self.name} (Size: {self.size}, Potency: {self.potency}): {self.description}"

class Weapon(Item):
    """Represents a generic weapon, inheriting from Item."""
    def __init__(self, name: str, description: str, size: int, power: int, range: int):
        super().__init__(name, description, size)
        self.power = power
        self.range = range

    def getPower(self) -> int:
        """Returns the power of the weapon."""
        return self.power

    def getRange(self) -> int:
        """Returns the range of the weapon."""
        return self.range
        
    def __str__(self) -> str:
        """Overrides the parent __str__ to include power and range."""
        return f"- {self.name} (Size: {self.size}, Power: {self.power}, Range: {self.range}): {self.description}"

# --- Weapon Subclasses ---
class Axe(Weapon):
    """Represents an Axe, inheriting from Weapon."""
    def __init__(self, name: str, size: int, power: int, range: int):
        # Initialize the parent Weapon class with a default description for an axe
        super().__init__(name, "A heavy, sharp axe made for cleaving.", size, power, range)

    def chop(self):
        """Generates a message for a chopping action."""
        print(f"You bring the {self.name} down with a mighty chop!")

    def swing(self):
        """Generates a message for a swinging action."""
        print(f"You swing the {self.name} in a wide arc.")

class Sword(Weapon):
    """Represents a Sword, inheriting from Weapon."""
    def __init__(self, name: str, size: int, power: int, range: int):
         # Initialize the parent Weapon class with a default description for a sword
        super().__init__(name, "A well-balanced sword with a keen edge.", size, power, range)
    
    def swing(self):
        """Generates a message for a swinging action."""
        print(f"You swing the {self.name} gracefully.")

    def thrust(self):
        """Generates a message for a thrusting action."""
        print(f"You thrust forward with the {self.name}!")

# --- Demonstration of the classes ---
if __name__ == "__main__":
    # 1. Create a pack
    my_pack = Pack(20)
    print(my_pack)
    print("\n" + "="*50 + "\n")

    # 2. Create some items
    health_potion = Potion(name="Lesser Health Potion", description="A simple brew that restores a small amount of health.", size=2, potency=25)
    great_axe = Axe(name="Greataxe of the Raider", size=8, power=15, range=2)
    longsword = Sword(name="Knight's Longsword", size=6, power=10, range=3)
    heavy_shield = Item(name="Iron Shield", description="A heavy shield providing excellent defense.", size=7) # Generic item

    # 3. Test adding items
    my_pack.addItem(health_potion)
    my_pack.addItem(great_axe)
    my_pack.addItem(longsword)
    
    # Try to add an item that won't fit
    my_pack.addItem(heavy_shield) 
    print("\n" + "="*50 + "\n")

    # 4. Print the pack contents
    print(my_pack)
    print("\n" + "="*50 + "\n")

    # 5. Test dropping items
    my_pack.dropItem(great_axe)
    
    # Try to drop an item that isn't in the pack
    my_pack.dropItem(heavy_shield)
    print(f"\nAfter dropping an item:\n{my_pack}\n")
    print("\n" + "="*50 + "\n")

    # 6. Test using methods on the items
    print("--- Testing Item Methods ---")
    health_potion.use()
    longsword.swing()
    longsword.thrust()
    # great_axe.chop() # This would fail now since we dropped it.
    
    # Let's add the shield now that there is space
    print("\n--- Trying to add the shield again ---")
    my_pack.addItem(heavy_shield)
    print(f"\n{my_pack}")