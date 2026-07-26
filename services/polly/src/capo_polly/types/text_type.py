"""Generated from Smithy shape ``com.amazonaws.polly#TextType``."""

from typing import Literal, TypeAlias, cast

TextType: TypeAlias = Literal[
    "ssml",
    "text",
]


# --- restJson1 ser/de ---
def serialize_json(value: TextType) -> str:
    return value


def deserialize_json(data: str) -> TextType:
    return cast(TextType, data)
