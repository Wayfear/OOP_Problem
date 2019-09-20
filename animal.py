class Animal:

    def __init__(self):
        self.name = None

    def call(self):
        raise NotImplementedError

    def whoAmI(self):
        print(f'I am a {self.name}')


class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.name = "Dog"

    def call(self):
        print("Bark!")


class Cat(Animal):

    def __init__(self):
        super().__init__()
        self.name = "Cat"

    def call(self):
        print("Meow!")


if __name__ == "__main__":
    dog = Dog()
    dog.call()
    dog.whoAmI()
    print("===============")

    cat = Cat()
    cat.call()
    cat.whoAmI()
