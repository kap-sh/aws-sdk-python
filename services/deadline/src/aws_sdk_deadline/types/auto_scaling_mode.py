"""Generated from Smithy shape ``com.amazonaws.deadline#AutoScalingMode``."""

from typing import Literal, TypeAlias, cast

AutoScalingMode: TypeAlias = Literal[
    "NO_SCALING",
    "EVENT_BASED_AUTO_SCALING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingMode) -> str:
    return value


def deserialize_json(data: str) -> AutoScalingMode:
    return cast(AutoScalingMode, data)
