

## E22MCAG0015
## Varnika Vyas

from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass
