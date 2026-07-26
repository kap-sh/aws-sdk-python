"""Generated from Smithy shape ``com.amazonaws.quicksight#DayOfTheWeek``."""

from typing import Literal, TypeAlias, cast

DayOfTheWeek: TypeAlias = Literal[
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DayOfTheWeek) -> str:
    return value


def deserialize_json(data: str) -> DayOfTheWeek:
    return cast(DayOfTheWeek, data)
