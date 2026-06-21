"""Generated from Smithy shape ``com.amazonaws.apigateway#ContentHandlingStrategy``."""

from typing import Literal, TypeAlias, cast

ContentHandlingStrategy: TypeAlias = Literal[
    "CONVERT_TO_BINARY",
    "CONVERT_TO_TEXT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentHandlingStrategy) -> str:
    return value


def deserialize_json(data: str) -> ContentHandlingStrategy:
    return cast(ContentHandlingStrategy, data)
