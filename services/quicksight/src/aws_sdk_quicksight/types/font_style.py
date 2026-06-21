"""Generated from Smithy shape ``com.amazonaws.quicksight#FontStyle``."""

from typing import Literal, TypeAlias, cast

FontStyle: TypeAlias = Literal[
    "NORMAL",
    "ITALIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: FontStyle) -> str:
    return value


def deserialize_json(data: str) -> FontStyle:
    return cast(FontStyle, data)
