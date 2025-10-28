from enum import Enum

class Mode(Enum):
    ASYM_OFF = 1
    SYM = 0
    ASYM_DEF = 2

print(type(Mode.SYM))
