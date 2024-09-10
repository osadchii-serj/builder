from abc import ABC, abstractmethod


class Robot(ABC):

    @abstractmethod
    def create_head(self):
        pass

    @abstractmethod
    def create_torso(self):
        pass

    @abstractmethod
    def create_arm_right(self):
        pass

    @abstractmethod
    def create_arm_left(self):
        pass

    @abstractmethod
    def create_leg_right(self):
        pass

    @abstractmethod
    def create_leg_left(self):
        pass
