"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInputs``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_input

FlowInputs: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.flow_input.FlowInput"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowInputs) -> list:
    import aws_sdk_bedrock_agent_runtime.types.flow_input
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.flow_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowInputs:
    import aws_sdk_bedrock_agent_runtime.types.flow_input
    out: FlowInputs = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.flow_input.deserialize_json(item))
    return out