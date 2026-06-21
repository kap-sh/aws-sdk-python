"""Generated from Smithy shape ``com.amazonaws.quicksight#TextTransform``."""

from typing import Literal, TypeAlias, cast

TextTransform: TypeAlias = Literal["CAPITALIZE",]


# --- restJson1 ser/de ---
def serialize_json(value: TextTransform) -> str:
    return value


def deserialize_json(data: str) -> TextTransform:
    return cast(TextTransform, data)
