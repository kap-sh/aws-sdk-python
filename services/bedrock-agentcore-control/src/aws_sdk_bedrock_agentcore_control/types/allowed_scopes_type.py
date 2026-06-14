"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AllowedScopesType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.allowed_scope_type

AllowedScopesType: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.allowed_scope_type.AllowedScopeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedScopesType) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedScopesType:
    return list(data)
