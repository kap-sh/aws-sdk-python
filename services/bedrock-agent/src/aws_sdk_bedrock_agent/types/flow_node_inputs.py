"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodeInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_input

FlowNodeInputs: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.flow_node_input.FlowNodeInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodeInputs) -> list:
    import aws_sdk_bedrock_agent.types.flow_node_input

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.flow_node_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowNodeInputs:
    import aws_sdk_bedrock_agent.types.flow_node_input

    out: FlowNodeInputs = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.flow_node_input.deserialize_json(item))
    return out
