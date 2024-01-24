# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#sldfdfdf######

class SweetPotato():
   def  __init__(self):
       self.cook_time = 0
       self.cook_static = 'raw'
       self.condiments = []


   def cook(self,time):
       self.cook_time += time
       if 0 <= self.cook_time <3:
           self.cook_static = 'raw'
       elif 3<= self.cook_time <5:
            self.cook_static = 'half raw'
       elif 5<= self.cook_time <8:
            self.cook_static = 'done'
       elif self.cook_time >= 8:
            self.cook_static = 'overdue'

   def add_condiments(self,condiment):
        self.condiments.append(condiment)


   def __str__(self):
        return f'this potats is {self.cook_time}, status is {self.cook_static}, tiaoliao {self.condiments}'



digua1 = SweetPotato()
print(digua1)
digua1.cook(5)
digua1.add_condiments('hujiao')
digua1.add_condiments('jiangyou')
print(digua1)















