"""Generated from Smithy shape ``com.amazonaws.macie2#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

DayOfWeek: TypeAlias = Literal[
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DayOfWeek) -> str:
    return value


def deserialize_json(data: str) -> DayOfWeek:
    return cast(DayOfWeek, data)
