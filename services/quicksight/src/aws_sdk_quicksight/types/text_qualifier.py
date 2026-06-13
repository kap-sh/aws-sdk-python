"""Generated from Smithy shape ``com.amazonaws.quicksight#TextQualifier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TextQualifier: TypeAlias = Literal[
    "DOUBLE_QUOTE",
    "SINGLE_QUOTE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOUBLE_QUOTE",
        "SINGLE_QUOTE",
    )
)


def serialize_json(value: TextQualifier) -> str:
    return value


def deserialize_json(data: str) -> TextQualifier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TextQualifier value: {data!r}")
    return cast(TextQualifier, data)
