"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeErrorCode``."""

from typing import Literal, TypeAlias, cast

NodeErrorCode: TypeAlias = Literal[
    "VALIDATION",
    "DEPENDENCY_FAILED",
    "BAD_GATEWAY",
    "INTERNAL_SERVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeErrorCode) -> str:
    return value


def deserialize_json(data: str) -> NodeErrorCode:
    return cast(NodeErrorCode, data)
