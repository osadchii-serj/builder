from optimus_prime import OptimusPrime
from interfaces import Robot


def client_code(robot: Robot):
    robot.start_assembly()
    robot.create_head()
    robot.create_torso()
    robot.create_arm_right()
    robot.create_arm_left()
    robot.create_leg_right()
    robot.create_leg_left()
    robot.finish_assembly()


optimus = OptimusPrime()
client_code(optimus)
