"""Generated from Smithy shape ``com.amazonaws.polly#TextType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

TextType: TypeAlias = Literal[
    "ssml",
    "text",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ssml",
        "text",
    )
)


def serialize_json(value: TextType) -> str:
    return value


def deserialize_json(data: str) -> TextType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TextType value: {data!r}")
    return cast(TextType, data)
