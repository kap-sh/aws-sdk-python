"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#AllowNotifications``."""

from typing import Literal, TypeAlias, cast

AllowNotifications: TypeAlias = Literal[
    "ALL",
    "NONE",
    "FILTERED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowNotifications) -> str:
    return value


def deserialize_json(data: str) -> AllowNotifications:
    return cast(AllowNotifications, data)
