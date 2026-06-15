"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OAuthScopes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.o_auth_scope

OAuthScopes: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.o_auth_scope.OAuthScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuthScopes) -> list:
    return list(value)


def deserialize_json(data: list) -> OAuthScopes:
    return list(data)
