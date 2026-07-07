"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MCPGatewayConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.mcp_instructions
    import aws_sdk_bedrock_agentcore_control.types.mcp_supported_versions
    import aws_sdk_bedrock_agentcore_control.types.search_type
    import aws_sdk_bedrock_agentcore_control.types.session_configuration
    import aws_sdk_bedrock_agentcore_control.types.streaming_configuration


class MCPGatewayConfiguration(TypedDict, closed=True):
    supported_versions: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.mcp_supported_versions.McpSupportedVersions"
    ]
    """<p>The supported versions of the Model Context Protocol. This field specifies which versions of the protocol the gateway can use.</p>"""
    instructions: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.mcp_instructions.McpInstructions"
    ]
    """<p>The instructions for using the Model Context Protocol gateway. These instructions provide guidance on how to interact with the gateway.</p>"""
    search_type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.search_type.SearchType"
    ]
    """<p>The search type for the Model Context Protocol gateway. This field specifies how the gateway handles search operations.</p>"""
    session_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.session_configuration.SessionConfiguration"
    ]
    """<p>The session configuration for the MCP gateway. This configuration controls session behavior, including session timeout settings.</p>"""
    streaming_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.streaming_configuration.StreamingConfiguration"
    ]
    """<p>The streaming configuration for the MCP gateway. This configuration controls whether response streaming is enabled for the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPGatewayConfiguration) -> dict:
    out: dict = {}
    if "supported_versions" in value:
        import aws_sdk_bedrock_agentcore_control.types.mcp_supported_versions

        out["supportedVersions"] = (
            aws_sdk_bedrock_agentcore_control.types.mcp_supported_versions.serialize_json(
                value["supported_versions"]
            )
        )
    if "instructions" in value:
        out["instructions"] = value["instructions"]
    if "search_type" in value:
        import aws_sdk_bedrock_agentcore_control.types.search_type

        out["searchType"] = (
            aws_sdk_bedrock_agentcore_control.types.search_type.serialize_json(
                value["search_type"]
            )
        )
    if "session_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.session_configuration

        out["sessionConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.session_configuration.serialize_json(
                value["session_configuration"]
            )
        )
    if "streaming_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.streaming_configuration

        out["streamingConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.streaming_configuration.serialize_json(
                value["streaming_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MCPGatewayConfiguration:
    out: MCPGatewayConfiguration = {}  # type: ignore[typeddict-item]
    if "supportedVersions" in data:
        import aws_sdk_bedrock_agentcore_control.types.mcp_supported_versions

        out["supported_versions"] = (
            aws_sdk_bedrock_agentcore_control.types.mcp_supported_versions.deserialize_json(
                data["supportedVersions"]
            )
        )
    if "instructions" in data:
        out["instructions"] = data["instructions"]
    if "searchType" in data:
        import aws_sdk_bedrock_agentcore_control.types.search_type

        out["search_type"] = (
            aws_sdk_bedrock_agentcore_control.types.search_type.deserialize_json(
                data["searchType"]
            )
        )
    if "sessionConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.session_configuration

        out["session_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.session_configuration.deserialize_json(
                data["sessionConfiguration"]
            )
        )
    if "streamingConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.streaming_configuration

        out["streaming_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.streaming_configuration.deserialize_json(
                data["streamingConfiguration"]
            )
        )
    return out
