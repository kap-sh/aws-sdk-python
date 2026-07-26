"""Generated from Smithy shape ``com.amazonaws.connect#ApplicationType``."""

from typing import Literal, TypeAlias, cast

ApplicationType: TypeAlias = Literal[
    "MCP",
    "THIRD_PARTY_APPLICATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    return cast(ApplicationType, data)
