"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Day``."""

from typing import Literal, TypeAlias, cast

Day: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: Day) -> str:
    return value


def deserialize_json(data: str) -> Day:
    return cast(Day, data)
