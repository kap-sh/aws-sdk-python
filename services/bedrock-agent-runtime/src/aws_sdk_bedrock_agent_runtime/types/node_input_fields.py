"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeInputFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.node_input_field

NodeInputFields: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.node_input_field.NodeInputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: NodeInputFields) -> list:
    import aws_sdk_bedrock_agent_runtime.types.node_input_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.node_input_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NodeInputFields:
    import aws_sdk_bedrock_agent_runtime.types.node_input_field

    out: NodeInputFields = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.node_input_field.deserialize_json(item)
        )
    return out
