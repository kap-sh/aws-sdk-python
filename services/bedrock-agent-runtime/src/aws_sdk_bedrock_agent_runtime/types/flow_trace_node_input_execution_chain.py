"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputExecutionChain``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item

FlowTraceNodeInputExecutionChain: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item.FlowTraceNodeInputExecutionChainItem"]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputExecutionChain) -> list:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowTraceNodeInputExecutionChain:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item
    out: FlowTraceNodeInputExecutionChain = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item.deserialize_json(item))
    return out