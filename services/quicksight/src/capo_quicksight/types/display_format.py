"""Generated from Smithy shape ``com.amazonaws.quicksight#DisplayFormat``."""

from typing import Literal, TypeAlias, cast

DisplayFormat: TypeAlias = Literal[
    "AUTO",
    "PERCENT",
    "CURRENCY",
    "NUMBER",
    "DATE",
    "STRING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DisplayFormat) -> str:
    return value


def deserialize_json(data: str) -> DisplayFormat:
    return cast(DisplayFormat, data)
