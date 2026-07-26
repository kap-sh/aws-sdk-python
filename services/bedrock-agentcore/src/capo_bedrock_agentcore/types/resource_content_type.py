"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResourceContentType``."""

from typing import Literal, TypeAlias, cast

ResourceContentType: TypeAlias = Literal[
    "text",
    "blob",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceContentType) -> str:
    return value


def deserialize_json(data: str) -> ResourceContentType:
    return cast(ResourceContentType, data)
