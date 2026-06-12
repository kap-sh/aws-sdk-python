"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionEvents``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_event

FlowExecutionEvents: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.flow_execution_event.FlowExecutionEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionEvents) -> list:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_event
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.flow_execution_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowExecutionEvents:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_event
    out: FlowExecutionEvents = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.flow_execution_event.deserialize_json(item))
    return out