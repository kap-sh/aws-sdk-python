"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceContentType``."""

from typing import Literal, TypeAlias, cast

UtteranceContentType: TypeAlias = Literal[
    "PlainText",
    "CustomPayload",
    "SSML",
    "ImageResponseCard",
]


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceContentType) -> str:
    return value


def deserialize_json(data: str) -> UtteranceContentType:
    return cast(UtteranceContentType, data)
