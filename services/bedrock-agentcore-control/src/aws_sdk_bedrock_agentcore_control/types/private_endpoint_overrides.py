"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivateEndpointOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint_override

PrivateEndpointOverrides: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.private_endpoint_override.PrivateEndpointOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateEndpointOverrides) -> list:
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.private_endpoint_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PrivateEndpointOverrides:
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint_override

    out: PrivateEndpointOverrides = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.private_endpoint_override.deserialize_json(
                item
            )
        )
    return out
