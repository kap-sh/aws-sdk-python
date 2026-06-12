"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node

FlowNodes: TypeAlias = list["aws_sdk_bedrock_agent.types.flow_node.FlowNode"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodes) -> list:
    import aws_sdk_bedrock_agent.types.flow_node

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.flow_node.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowNodes:
    import aws_sdk_bedrock_agent.types.flow_node

    out: FlowNodes = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.flow_node.deserialize_json(item))
    return out
