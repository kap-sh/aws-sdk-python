"""Generated from Smithy shape ``com.amazonaws.inspector2#Day``."""

from typing import Literal, TypeAlias, cast

Day: TypeAlias = Literal[
    "SUN",
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Day) -> str:
    return value


def deserialize_json(data: str) -> Day:
    return cast(Day, data)
