"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TimeDimension``."""

from typing import Literal, TypeAlias, cast

TimeDimension: TypeAlias = Literal[
    "Hours",
    "Days",
    "Weeks",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeDimension) -> str:
    return value


def deserialize_json(data: str) -> TimeDimension:
    return cast(TimeDimension, data)
