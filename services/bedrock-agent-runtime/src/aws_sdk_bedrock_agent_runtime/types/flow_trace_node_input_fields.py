"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_field

FlowTraceNodeInputFields: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_field.FlowTraceNodeInputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputFields) -> list:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FlowTraceNodeInputFields:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_field

    out: FlowTraceNodeInputFields = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_field.deserialize_json(
                item
            )
        )
    return out
