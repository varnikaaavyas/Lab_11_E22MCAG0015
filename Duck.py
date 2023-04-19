
## E22MCAG0015
## Varnika Vyas



from abc import ABC, abstractmethod

from FlyBehavior import FlyBehavior
from QuackBehavior import QuackBehavior


class Duck(ABC):
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    def swim(self):
        print("All ducks CAN swim, even decoys!")

    @abstractmethod
    def display(self):
        pass

    def perform_fly_behavior(self):
        self.fly_behavior.fly()

    def perform_quack_behavior(self):
        self.quack_behavior.quack()
