"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSystemPrompt``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_system_content_block

HarnessSystemPrompt: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.harness_system_content_block.HarnessSystemContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSystemPrompt) -> list:
    import aws_sdk_bedrock_agentcore_control.types.harness_system_content_block

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.harness_system_content_block.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HarnessSystemPrompt:
    import aws_sdk_bedrock_agentcore_control.types.harness_system_content_block

    out: HarnessSystemPrompt = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.harness_system_content_block.deserialize_json(
                item
            )
        )
    return out
