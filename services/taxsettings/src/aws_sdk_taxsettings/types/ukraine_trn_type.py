"""Generated from Smithy shape ``com.amazonaws.taxsettings#UkraineTrnType``."""

from typing import Literal, TypeAlias, cast

UkraineTrnType: TypeAlias = Literal[
    "Business",
    "Individual",
]


# --- restJson1 ser/de ---
def serialize_json(value: UkraineTrnType) -> str:
    return value


def deserialize_json(data: str) -> UkraineTrnType:
    return cast(UkraineTrnType, data)
