"""Generated from Smithy shape ``com.amazonaws.connect#OverrideDays``."""

from typing import Literal, TypeAlias, cast

OverrideDays: TypeAlias = Literal[
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: OverrideDays) -> str:
    return value


def deserialize_json(data: str) -> OverrideDays:
    return cast(OverrideDays, data)
