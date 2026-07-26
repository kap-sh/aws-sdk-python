"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_content_block

HarnessContentBlocks: TypeAlias = list[
    "capo_bedrock_agentcore.types.harness_content_block.HarnessContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlocks) -> list:
    import capo_bedrock_agentcore.types.harness_content_block

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.harness_content_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarnessContentBlocks:
    import capo_bedrock_agentcore.types.harness_content_block

    out: HarnessContentBlocks = []
    for item in data:
        out.append(
            capo_bedrock_agentcore.types.harness_content_block.deserialize_json(item)
        )
    return out
