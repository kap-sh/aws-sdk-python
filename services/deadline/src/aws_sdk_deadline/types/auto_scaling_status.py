"""Generated from Smithy shape ``com.amazonaws.deadline#AutoScalingStatus``."""

from typing import Literal, TypeAlias, cast

AutoScalingStatus: TypeAlias = Literal[
    "GROWING",
    "STEADY",
    "SHRINKING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoScalingStatus:
    return cast(AutoScalingStatus, data)
