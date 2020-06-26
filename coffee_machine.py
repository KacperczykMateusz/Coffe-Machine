class CoffeeMachine:
    def __init__(self):
        self.products = ['water', 'milk', 'beans', 'cups', 'money']
        self.quantity = [400, 540, 120, 9, 550]  # ingredients at start
        self.espresso_rec = [250, 0, 16, 1, 4]  # espresso recipe
        self.latte_rec = [350, 75, 20, 1, 7]  # latte recipe
        self.cappuccino_rec = [200, 100, 12, 1, 6]  # cappuccino recipe

    # print available stock
    def machine_has(self):
        print('The coffee machine has:')
        for a in range(4):
            print(self.quantity[a], 'of', self.products[a])
        print('$' + str(self.quantity[4]), 'of money')

    # checking ingredients needed to do action
    def check_quantity(self, coffee):
        for b in range(4):
            if self.quantity[b] < coffee[b]:
                print('Sorry, not enough', self.products[b] + '!')
                return
        print('I have enough resources, making you a coffee!')
        for c in range(4):
            self.quantity[c] -= coffee[c]
        self.quantity[4] += coffee[4]

    # all actions after choosing buy option from main menu
    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        choose = input('> ')
        if choose == '1':
            self.check_quantity(self.espresso_rec)
        elif choose == '2':
            self.check_quantity(self.latte_rec)
        elif choose == '3':
            self.check_quantity(self.cappuccino_rec)
        else:
            return

    # take money from the machine
    def take(self):
        print('I gave you', self.quantity[4])
        self.quantity[4] = 0

    # refill stock machine
    def fill(self):
        for e in range(4):
            if e == 2:
                print('Write how many grams of', self.products[e], 'do you want to add:')
            elif e == 3:
                print('Write how many disposable', self.products[e], 'do you want to add:')
            else:
                print('Write how many ml of', self.products[e], 'do you want to add:')
            self.quantity[e] += int(input('> '))

    def action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            action = input('> ')
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.machine_has()
            elif action == 'exit':
                print('Thank You')
                break
            print()


CoffeeMachine().action()
