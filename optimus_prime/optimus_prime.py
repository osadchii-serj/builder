from interfaces import Robot


class OptimusPrime(Robot):

    def __init__(self) -> None:
        self.__name = "OptimusPrime"
        self.__arm_right = None
        self.__leg_right = None
        self.__arm_left = None
        self.__leg_left = None
        self.__head = None
        self.__torso = None

    def __str__(self) -> str:
        return f"Робот {self.__name}"

    def start_assembly(self):
        print("Запуск сборки ...")

    def create_head(self):
        self.__head = "Голова"
        print(f"Создана {self.__head} робота")
        return self

    def create_torso(self):
        self.__torso = "Тело"
        print(f"Создано {self.__torso} робота")
        return self

    def create_arm_right(self):
        self.__arm_right = "Правая рука"
        print(f"Создана {self.__arm_right} робота")
        return self

    def create_arm_left(self):
        self.__arm_left = "Левая рука"
        print(f"Создана {self.__arm_left} робота")
        return self

    def create_leg_right(self):
        self.__leg_right = "Правая нога"
        print(f"Создана {self.__leg_right} робота")
        return self

    def create_leg_left(self):
        self.__leg_left = "Левая нога"
        print(f"Создана {self.__leg_left} робота")
        return self

    def finish_assembly(self):
        print(f"Сборка завершена - {self} готов.")
