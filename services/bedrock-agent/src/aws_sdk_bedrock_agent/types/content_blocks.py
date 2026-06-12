"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ContentBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.content_block

ContentBlocks: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.content_block.ContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlocks) -> list:
    import aws_sdk_bedrock_agent.types.content_block

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.content_block.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContentBlocks:
    import aws_sdk_bedrock_agent.types.content_block

    out: ContentBlocks = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.content_block.deserialize_json(item))
    return out
