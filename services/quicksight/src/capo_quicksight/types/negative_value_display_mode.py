"""Generated from Smithy shape ``com.amazonaws.quicksight#NegativeValueDisplayMode``."""

from typing import Literal, TypeAlias, cast

NegativeValueDisplayMode: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NegativeValueDisplayMode) -> str:
    return value


def deserialize_json(data: str) -> NegativeValueDisplayMode:
    return cast(NegativeValueDisplayMode, data)
