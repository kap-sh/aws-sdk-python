"""Generated from Smithy shape ``com.amazonaws.iot#ViolationEventType``."""

from typing import Literal, TypeAlias, cast

ViolationEventType: TypeAlias = Literal[
    "in-alarm",
    "alarm-cleared",
    "alarm-invalidated",
]


# --- restJson1 ser/de ---
def serialize_json(value: ViolationEventType) -> str:
    return value


def deserialize_json(data: str) -> ViolationEventType:
    return cast(ViolationEventType, data)
