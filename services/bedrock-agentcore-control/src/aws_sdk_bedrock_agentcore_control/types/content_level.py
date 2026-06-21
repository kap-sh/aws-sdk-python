"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ContentLevel``."""

from typing import Literal, TypeAlias, cast

ContentLevel: TypeAlias = Literal[
    "METADATA_ONLY",
    "FULL_CONTENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentLevel) -> str:
    return value


def deserialize_json(data: str) -> ContentLevel:
    return cast(ContentLevel, data)
