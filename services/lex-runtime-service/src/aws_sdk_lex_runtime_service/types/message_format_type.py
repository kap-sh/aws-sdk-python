"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#MessageFormatType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_service.errors import DeserializationError

MessageFormatType: TypeAlias = Literal[
    "PlainText",
    "CustomPayload",
    "SSML",
    "Composite",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PlainText",
        "CustomPayload",
        "SSML",
        "Composite",
    )
)


def serialize_json(value: MessageFormatType) -> str:
    return value


def deserialize_json(data: str) -> MessageFormatType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageFormatType value: {data!r}")
    return cast(MessageFormatType, data)
