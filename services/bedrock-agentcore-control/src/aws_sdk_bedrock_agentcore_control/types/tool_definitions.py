"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ToolDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.tool_definition

ToolDefinitions: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.tool_definition.ToolDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolDefinitions) -> list:
    import aws_sdk_bedrock_agentcore_control.types.tool_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.tool_definition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ToolDefinitions:
    import aws_sdk_bedrock_agentcore_control.types.tool_definition

    out: ToolDefinitions = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.tool_definition.deserialize_json(
                item
            )
        )
    return out
