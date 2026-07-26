"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#MessageContentType``."""

from typing import Literal, TypeAlias, cast

MessageContentType: TypeAlias = Literal[
    "CustomPayload",
    "ImageResponseCard",
    "PlainText",
    "SSML",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageContentType) -> str:
    return value


def deserialize_json(data: str) -> MessageContentType:
    return cast(MessageContentType, data)
