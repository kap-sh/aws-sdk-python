"""Generated from Smithy shape ``com.amazonaws.iot#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

DayOfWeek: TypeAlias = Literal[
    "SUN",
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DayOfWeek) -> str:
    return value


def deserialize_json(data: str) -> DayOfWeek:
    return cast(DayOfWeek, data)
