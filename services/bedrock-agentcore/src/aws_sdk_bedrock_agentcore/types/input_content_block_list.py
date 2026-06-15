"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InputContentBlockList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.input_content_block

InputContentBlockList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.input_content_block.InputContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: InputContentBlockList) -> list:
    import aws_sdk_bedrock_agentcore.types.input_content_block

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.input_content_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InputContentBlockList:
    import aws_sdk_bedrock_agentcore.types.input_content_block

    out: InputContentBlockList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.input_content_block.deserialize_json(item)
        )
    return out
