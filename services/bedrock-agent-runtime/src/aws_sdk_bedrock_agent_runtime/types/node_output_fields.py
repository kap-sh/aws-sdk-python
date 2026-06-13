"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeOutputFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.node_output_field

NodeOutputFields: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.node_output_field.NodeOutputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeOutputFields) -> list:
    import aws_sdk_bedrock_agent_runtime.types.node_output_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.node_output_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NodeOutputFields:
    import aws_sdk_bedrock_agent_runtime.types.node_output_field

    out: NodeOutputFields = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.node_output_field.deserialize_json(item)
        )
    return out
