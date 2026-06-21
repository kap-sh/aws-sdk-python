"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ContentBlockType``."""

from typing import Literal, TypeAlias, cast

ContentBlockType: TypeAlias = Literal[
    "text",
    "image",
    "resource",
    "resource_link",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockType) -> str:
    return value


def deserialize_json(data: str) -> ContentBlockType:
    return cast(ContentBlockType, data)
