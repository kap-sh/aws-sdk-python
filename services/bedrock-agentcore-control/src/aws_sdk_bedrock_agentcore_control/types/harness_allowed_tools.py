"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAllowedTools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_allowed_tool

HarnessAllowedTools: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.harness_allowed_tool.HarnessAllowedTool"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAllowedTools) -> list:
    return list(value)


def deserialize_json(data: list) -> HarnessAllowedTools:
    return list(data)
