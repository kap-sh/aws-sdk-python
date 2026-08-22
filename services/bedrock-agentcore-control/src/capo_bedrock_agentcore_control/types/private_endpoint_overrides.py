"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivateEndpointOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.private_endpoint_override

PrivateEndpointOverrides: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.private_endpoint_override.PrivateEndpointOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateEndpointOverrides) -> list:
    import capo_bedrock_agentcore_control.types.private_endpoint_override

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.private_endpoint_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PrivateEndpointOverrides:
    import capo_bedrock_agentcore_control.types.private_endpoint_override

    out: PrivateEndpointOverrides = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.private_endpoint_override.deserialize_json(
                item
            )
        )
    return out
