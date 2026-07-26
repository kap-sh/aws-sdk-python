"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Role``."""

from typing import Literal, TypeAlias, cast

Role: TypeAlias = Literal[
    "ASSISTANT",
    "USER",
    "TOOL",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: Role) -> str:
    return value


def deserialize_json(data: str) -> Role:
    return cast(Role, data)
