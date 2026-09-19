from enum import Enum
from dataclasses import dataclass


class CommandType(Enum):
    MOVE_FORWARD = 1
    TURN_LEFT = 2
    TURN_RIGHT = 3
    MOVE_BACKWARD = 4


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Command:
    type: CommandType
    steps: int
