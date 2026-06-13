"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeInputExecutionChain``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain_item

NodeInputExecutionChain: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain_item.NodeInputExecutionChainItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeInputExecutionChain) -> list:
    import aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NodeInputExecutionChain:
    import aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain_item

    out: NodeInputExecutionChain = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain_item.deserialize_json(
                item
            )
        )
    return out
