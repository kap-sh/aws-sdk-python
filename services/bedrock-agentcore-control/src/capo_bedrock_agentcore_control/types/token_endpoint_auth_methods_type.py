"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TokenEndpointAuthMethodsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.token_auth_method

TokenEndpointAuthMethodsType: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.token_auth_method.TokenAuthMethod"
]


# --- restJson1 ser/de ---
def serialize_json(value: TokenEndpointAuthMethodsType) -> list:
    return list(value)


def deserialize_json(data: list) -> TokenEndpointAuthMethodsType:
    return list(data)
