"""Generated from Smithy shape ``com.amazonaws.quicksight#UndefinedSpecifiedValueType``."""

from typing import Literal, TypeAlias, cast

UndefinedSpecifiedValueType: TypeAlias = Literal[
    "LEAST",
    "MOST",
]


# --- restJson1 ser/de ---
def serialize_json(value: UndefinedSpecifiedValueType) -> str:
    return value


def deserialize_json(data: str) -> UndefinedSpecifiedValueType:
    return cast(UndefinedSpecifiedValueType, data)
