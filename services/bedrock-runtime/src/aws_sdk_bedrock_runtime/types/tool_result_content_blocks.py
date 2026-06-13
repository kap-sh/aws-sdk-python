"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultContentBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.tool_result_content_block

ToolResultContentBlocks: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.tool_result_content_block.ToolResultContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultContentBlocks) -> list:
    import aws_sdk_bedrock_runtime.types.tool_result_content_block

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.tool_result_content_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ToolResultContentBlocks:
    import aws_sdk_bedrock_runtime.types.tool_result_content_block

    out: ToolResultContentBlocks = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.tool_result_content_block.deserialize_json(
                item
            )
        )
    return out
