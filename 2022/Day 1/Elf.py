class Elf:
    inventory = []
    totalCals = 0

    def addInventory(self, item):
        item = int(item)
        self.inventory.append(item)
        self.totalCals += item