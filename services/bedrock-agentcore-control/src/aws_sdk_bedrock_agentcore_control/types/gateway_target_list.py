"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_target

GatewayTargetList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.gateway_target.GatewayTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayTargetList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.gateway_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.gateway_target.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GatewayTargetList:
    import aws_sdk_bedrock_agentcore_control.types.gateway_target

    out: GatewayTargetList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.gateway_target.deserialize_json(
                item
            )
        )
    return out
