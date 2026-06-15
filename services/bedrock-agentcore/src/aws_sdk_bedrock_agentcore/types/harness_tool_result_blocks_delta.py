"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultBlocksDelta``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_block_delta

HarnessToolResultBlocksDelta: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.harness_tool_result_block_delta.HarnessToolResultBlockDelta"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultBlocksDelta) -> list:
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_block_delta

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.harness_tool_result_block_delta.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HarnessToolResultBlocksDelta:
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_block_delta

    out: HarnessToolResultBlocksDelta = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.harness_tool_result_block_delta.deserialize_json(
                item
            )
        )
    return out
