"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceConditions``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_condition

FlowTraceConditions: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.flow_trace_condition.FlowTraceCondition"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceConditions) -> list:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_condition
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.flow_trace_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowTraceConditions:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_condition
    out: FlowTraceConditions = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.flow_trace_condition.deserialize_json(item))
    return out