"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpSupportedVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.mcp_version

McpSupportedVersions: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.mcp_version.McpVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: McpSupportedVersions) -> list:
    return list(value)


def deserialize_json(data: list) -> McpSupportedVersions:
    return [item for item in data if item is not None]
