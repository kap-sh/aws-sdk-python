"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ContentBlockList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.content_block

ContentBlockList: TypeAlias = list[
    "capo_bedrock_agentcore.types.content_block.ContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockList) -> list:
    import capo_bedrock_agentcore.types.content_block

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.content_block.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContentBlockList:
    import capo_bedrock_agentcore.types.content_block

    out: ContentBlockList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.content_block.deserialize_json(item))
    return out
