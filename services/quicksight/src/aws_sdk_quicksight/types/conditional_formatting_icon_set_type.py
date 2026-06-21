"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingIconSetType``."""

from typing import Literal, TypeAlias, cast

ConditionalFormattingIconSetType: TypeAlias = Literal[
    "PLUS_MINUS",
    "CHECK_X",
    "THREE_COLOR_ARROW",
    "THREE_GRAY_ARROW",
    "CARET_UP_MINUS_DOWN",
    "THREE_SHAPE",
    "THREE_CIRCLE",
    "FLAGS",
    "BARS",
    "FOUR_COLOR_ARROW",
    "FOUR_GRAY_ARROW",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingIconSetType) -> str:
    return value


def deserialize_json(data: str) -> ConditionalFormattingIconSetType:
    return cast(ConditionalFormattingIconSetType, data)
