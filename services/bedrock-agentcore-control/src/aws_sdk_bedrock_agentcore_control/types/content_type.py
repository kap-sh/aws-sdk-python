"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ContentType``."""

from typing import Literal, TypeAlias, cast

ContentType: TypeAlias = Literal["MEMORY_RECORDS",]


# --- restJson1 ser/de ---
def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    return cast(ContentType, data)
