"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpSupportedVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.mcp_version

McpSupportedVersions: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.mcp_version.McpVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: McpSupportedVersions) -> list:
    return list(value)


def deserialize_json(data: list) -> McpSupportedVersions:
    return list(data)
