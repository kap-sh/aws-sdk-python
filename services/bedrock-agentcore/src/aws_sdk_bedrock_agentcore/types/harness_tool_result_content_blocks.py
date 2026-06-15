"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultContentBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_content_block

HarnessToolResultContentBlocks: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.harness_tool_result_content_block.HarnessToolResultContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultContentBlocks) -> list:
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_content_block

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.harness_tool_result_content_block.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HarnessToolResultContentBlocks:
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_content_block

    out: HarnessToolResultContentBlocks = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.harness_tool_result_content_block.deserialize_json(
                item
            )
        )
    return out
