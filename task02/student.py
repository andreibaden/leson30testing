from human import Human

class Student(Human):
    def hello(self):
        super().hello()
        print()


def main():
    h = Human("trueman")
    st = Student("Alex")
    h.hello()
    st.hello()