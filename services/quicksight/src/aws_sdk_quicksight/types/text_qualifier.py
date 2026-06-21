"""Generated from Smithy shape ``com.amazonaws.quicksight#TextQualifier``."""

from typing import Literal, TypeAlias, cast

TextQualifier: TypeAlias = Literal[
    "DOUBLE_QUOTE",
    "SINGLE_QUOTE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TextQualifier) -> str:
    return value


def deserialize_json(data: str) -> TextQualifier:
    return cast(TextQualifier, data)
