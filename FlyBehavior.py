## E22MCAG0015
## Varnika Vyas



from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass
