"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.http_target_configuration
    import capo_bedrock_agentcore_control.types.mcp_target_configuration


class _TargetConfiguration_mcp(TypedDict, closed=True):
    mcp: "capo_bedrock_agentcore_control.types.mcp_target_configuration.McpTargetConfiguration"


class _TargetConfiguration_http(TypedDict, closed=True):
    http: "capo_bedrock_agentcore_control.types.http_target_configuration.HttpTargetConfiguration"


TargetConfiguration: TypeAlias = _TargetConfiguration_mcp | _TargetConfiguration_http


# --- restJson1 ser/de ---
def serialize_json(value: TargetConfiguration) -> dict:
    if "mcp" in value:
        import capo_bedrock_agentcore_control.types.mcp_target_configuration

        return {
            "mcp": capo_bedrock_agentcore_control.types.mcp_target_configuration.serialize_json(
                value["mcp"]
            )
        }
    elif "http" in value:
        import capo_bedrock_agentcore_control.types.http_target_configuration

        return {
            "http": capo_bedrock_agentcore_control.types.http_target_configuration.serialize_json(
                value["http"]
            )
        }
    else:
        raise SerializationError("TargetConfiguration: no variant present")


def deserialize_json(data: dict) -> TargetConfiguration:
    if "mcp" in data:
        import capo_bedrock_agentcore_control.types.mcp_target_configuration

        return {
            "mcp": capo_bedrock_agentcore_control.types.mcp_target_configuration.deserialize_json(
                data["mcp"]
            )
        }
    elif "http" in data:
        import capo_bedrock_agentcore_control.types.http_target_configuration

        return {
            "http": capo_bedrock_agentcore_control.types.http_target_configuration.deserialize_json(
                data["http"]
            )
        }
    else:
        raise DeserializationError("TargetConfiguration: no recognized variant key")
