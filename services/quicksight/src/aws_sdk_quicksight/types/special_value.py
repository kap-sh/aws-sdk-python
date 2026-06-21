"""Generated from Smithy shape ``com.amazonaws.quicksight#SpecialValue``."""

from typing import Literal, TypeAlias, cast

SpecialValue: TypeAlias = Literal[
    "EMPTY",
    "NULL",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: SpecialValue) -> str:
    return value


def deserialize_json(data: str) -> SpecialValue:
    return cast(SpecialValue, data)
