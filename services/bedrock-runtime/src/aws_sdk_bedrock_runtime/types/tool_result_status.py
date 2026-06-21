"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultStatus``."""

from typing import Literal, TypeAlias, cast

ToolResultStatus: TypeAlias = Literal[
    "success",
    "error",
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultStatus) -> str:
    return value


def deserialize_json(data: str) -> ToolResultStatus:
    return cast(ToolResultStatus, data)
