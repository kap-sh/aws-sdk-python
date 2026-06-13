"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingIconSetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ConditionalFormattingIconSetType) -> str:
    return value


def deserialize_json(data: str) -> ConditionalFormattingIconSetType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConditionalFormattingIconSetType value: {data!r}"
        )
    return cast(ConditionalFormattingIconSetType, data)
