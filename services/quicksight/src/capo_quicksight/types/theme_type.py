"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeType``."""

from typing import Literal, TypeAlias, cast

ThemeType: TypeAlias = Literal[
    "QUICKSIGHT",
    "CUSTOM",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeType) -> str:
    return value


def deserialize_json(data: str) -> ThemeType:
    return cast(ThemeType, data)
