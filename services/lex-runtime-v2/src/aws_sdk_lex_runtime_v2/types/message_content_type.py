"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#MessageContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

MessageContentType: TypeAlias = Literal[
    "CustomPayload",
    "ImageResponseCard",
    "PlainText",
    "SSML",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CustomPayload",
        "ImageResponseCard",
        "PlainText",
        "SSML",
    )
)


def serialize_json(value: MessageContentType) -> str:
    return value


def deserialize_json(data: str) -> MessageContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageContentType value: {data!r}")
    return cast(MessageContentType, data)
