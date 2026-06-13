"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeOutputNextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.node_output_next

NodeOutputNextList: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.node_output_next.NodeOutputNext"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeOutputNextList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.node_output_next

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.node_output_next.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NodeOutputNextList:
    import aws_sdk_bedrock_agent_runtime.types.node_output_next

    out: NodeOutputNextList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.node_output_next.deserialize_json(item)
        )
    return out
