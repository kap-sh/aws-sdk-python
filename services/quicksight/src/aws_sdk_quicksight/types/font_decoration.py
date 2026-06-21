"""Generated from Smithy shape ``com.amazonaws.quicksight#FontDecoration``."""

from typing import Literal, TypeAlias, cast

FontDecoration: TypeAlias = Literal[
    "UNDERLINE",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FontDecoration) -> str:
    return value


def deserialize_json(data: str) -> FontDecoration:
    return cast(FontDecoration, data)
