"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#MessageFormatType``."""

from typing import Literal, TypeAlias, cast

MessageFormatType: TypeAlias = Literal[
    "PlainText",
    "CustomPayload",
    "SSML",
    "Composite",
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageFormatType) -> str:
    return value


def deserialize_json(data: str) -> MessageFormatType:
    return cast(MessageFormatType, data)
