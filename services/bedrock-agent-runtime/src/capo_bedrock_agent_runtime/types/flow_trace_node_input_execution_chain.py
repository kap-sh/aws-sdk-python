"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputExecutionChain``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item

FlowTraceNodeInputExecutionChain: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item.FlowTraceNodeInputExecutionChainItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputExecutionChain) -> list:
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FlowTraceNodeInputExecutionChain:
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item

    out: FlowTraceNodeInputExecutionChain = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain_item.deserialize_json(
                item
            )
        )
    return out
