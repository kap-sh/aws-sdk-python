"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_field

FlowTraceNodeOutputFields: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_field.FlowTraceNodeOutputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputFields) -> list:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FlowTraceNodeOutputFields:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_field

    out: FlowTraceNodeOutputFields = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_field.deserialize_json(
                item
            )
        )
    return out
