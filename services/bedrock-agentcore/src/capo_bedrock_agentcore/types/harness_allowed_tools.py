"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessAllowedTools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_allowed_tool

HarnessAllowedTools: TypeAlias = list[
    "capo_bedrock_agentcore.types.harness_allowed_tool.HarnessAllowedTool"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAllowedTools) -> list:
    return list(value)


def deserialize_json(data: list) -> HarnessAllowedTools:
    return list(data)
