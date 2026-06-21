"""Generated from Smithy shape ``com.amazonaws.connect#RecurrenceFrequency``."""

from typing import Literal, TypeAlias, cast

RecurrenceFrequency: TypeAlias = Literal[
    "WEEKLY",
    "MONTHLY",
    "YEARLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecurrenceFrequency) -> str:
    return value


def deserialize_json(data: str) -> RecurrenceFrequency:
    return cast(RecurrenceFrequency, data)
