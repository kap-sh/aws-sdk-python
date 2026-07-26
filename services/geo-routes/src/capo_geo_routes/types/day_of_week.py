"""Generated from Smithy shape ``com.amazonaws.georoutes#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

DayOfWeek: TypeAlias = Literal[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


# --- restJson1 ser/de ---
def serialize_json(value: DayOfWeek) -> str:
    return value


def deserialize_json(data: str) -> DayOfWeek:
    return cast(DayOfWeek, data)
