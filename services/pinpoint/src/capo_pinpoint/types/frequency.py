"""Generated from Smithy shape ``com.amazonaws.pinpoint#Frequency``."""

from typing import Literal, TypeAlias, cast

Frequency: TypeAlias = Literal[
    "ONCE",
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
    "EVENT",
    "IN_APP_EVENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Frequency) -> str:
    return value


def deserialize_json(data: str) -> Frequency:
    return cast(Frequency, data)
