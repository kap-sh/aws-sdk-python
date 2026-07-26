"""Generated from Smithy shape ``com.amazonaws.quicksight#TextWrap``."""

from typing import Literal, TypeAlias, cast

TextWrap: TypeAlias = Literal[
    "NONE",
    "WRAP",
]


# --- restJson1 ser/de ---
def serialize_json(value: TextWrap) -> str:
    return value


def deserialize_json(data: str) -> TextWrap:
    return cast(TextWrap, data)
