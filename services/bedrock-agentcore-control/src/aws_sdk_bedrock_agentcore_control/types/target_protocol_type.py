"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetProtocolType``."""

from typing import Literal, TypeAlias, cast

TargetProtocolType: TypeAlias = Literal[
    "MCP",
    "HTTP",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetProtocolType) -> str:
    return value


def deserialize_json(data: str) -> TargetProtocolType:
    return cast(TargetProtocolType, data)
