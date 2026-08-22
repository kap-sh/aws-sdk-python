"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodeOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_output

FlowNodeOutputs: TypeAlias = list[
    "capo_bedrock_agent.types.flow_node_output.FlowNodeOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodeOutputs) -> list:
    import capo_bedrock_agent.types.flow_node_output

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.flow_node_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowNodeOutputs:
    import capo_bedrock_agent.types.flow_node_output

    out: FlowNodeOutputs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.flow_node_output.deserialize_json(item))
    return out
