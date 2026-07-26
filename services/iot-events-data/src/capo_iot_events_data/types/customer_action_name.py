"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#CustomerActionName``."""

from typing import Literal, TypeAlias, cast

CustomerActionName: TypeAlias = Literal[
    "SNOOZE",
    "ENABLE",
    "DISABLE",
    "ACKNOWLEDGE",
    "RESET",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerActionName) -> str:
    return value


def deserialize_json(data: str) -> CustomerActionName:
    return cast(CustomerActionName, data)
