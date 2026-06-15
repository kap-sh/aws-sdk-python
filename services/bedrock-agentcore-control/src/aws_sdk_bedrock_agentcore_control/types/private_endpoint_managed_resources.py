"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivateEndpointManagedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.managed_resource_details

PrivateEndpointManagedResources: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.managed_resource_details.ManagedResourceDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateEndpointManagedResources) -> list:
    import aws_sdk_bedrock_agentcore_control.types.managed_resource_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.managed_resource_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PrivateEndpointManagedResources:
    import aws_sdk_bedrock_agentcore_control.types.managed_resource_details

    out: PrivateEndpointManagedResources = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.managed_resource_details.deserialize_json(
                item
            )
        )
    return out
