"""Generated from Smithy shape ``com.amazonaws.quicksight#FontWeightName``."""

from typing import Literal, TypeAlias, cast

FontWeightName: TypeAlias = Literal[
    "NORMAL",
    "BOLD",
]


# --- restJson1 ser/de ---
def serialize_json(value: FontWeightName) -> str:
    return value


def deserialize_json(data: str) -> FontWeightName:
    return cast(FontWeightName, data)
