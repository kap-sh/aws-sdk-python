"""Generated from Smithy shape ``com.amazonaws.deadline#Period``."""

from typing import Literal, TypeAlias, cast

Period: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: Period) -> str:
    return value


def deserialize_json(data: str) -> Period:
    return cast(Period, data)
