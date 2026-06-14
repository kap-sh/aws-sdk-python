"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.tool_description_output

ToolDescriptionResultList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.tool_description_output.ToolDescriptionOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionResultList) -> list:
    import aws_sdk_bedrock_agentcore.types.tool_description_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.tool_description_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ToolDescriptionResultList:
    import aws_sdk_bedrock_agentcore.types.tool_description_output

    out: ToolDescriptionResultList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.tool_description_output.deserialize_json(
                item
            )
        )
    return out
