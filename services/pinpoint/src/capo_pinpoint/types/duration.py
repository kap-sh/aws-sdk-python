"""Generated from Smithy shape ``com.amazonaws.pinpoint#Duration``."""

from typing import Literal, TypeAlias, cast

Duration: TypeAlias = Literal[
    "HR_24",
    "DAY_7",
    "DAY_14",
    "DAY_30",
]


# --- restJson1 ser/de ---
def serialize_json(value: Duration) -> str:
    return value


def deserialize_json(data: str) -> Duration:
    return cast(Duration, data)
