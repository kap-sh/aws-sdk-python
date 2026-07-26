"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpServerTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.listing_mode
    import capo_bedrock_agentcore_control.types.mcp_tool_schema_configuration
    import capo_bedrock_agentcore_control.types.target_resource_priority


class McpServerTargetConfiguration(TypedDict, closed=True):
    endpoint: "str"
    """<p>The endpoint for the MCP server target configuration.</p>"""
    mcp_tool_schema: NotRequired[
        "capo_bedrock_agentcore_control.types.mcp_tool_schema_configuration.McpToolSchemaConfiguration"
    ]
    """<p>The tool schema configuration for the MCP server target. Supported only when the credential provider is configured with an authorization code grant type. Dynamic tool discovery/synchronization will be disabled when target is configured with mcpToolSchema.</p>"""
    listing_mode: NotRequired[
        "capo_bedrock_agentcore_control.types.listing_mode.ListingMode"
    ]
    """<p>The listing mode for the MCP server target configuration. MCP resources for default targets are cached at the control plane for faster access. MCP resources for dynamic targets will be dynamically retrieved when listing tools.</p>"""
    resource_priority: NotRequired[
        "capo_bedrock_agentcore_control.types.target_resource_priority.TargetResourcePriority"
    ]
    """<p>Priority for resolving MCP server targets with shared resource URIs. Lower values take precedence. Defaults to 1000 when not set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: McpServerTargetConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    if "mcp_tool_schema" in value:
        import capo_bedrock_agentcore_control.types.mcp_tool_schema_configuration

        out["mcpToolSchema"] = (
            capo_bedrock_agentcore_control.types.mcp_tool_schema_configuration.serialize_json(
                value["mcp_tool_schema"]
            )
        )
    if "listing_mode" in value:
        import capo_bedrock_agentcore_control.types.listing_mode

        out["listingMode"] = (
            capo_bedrock_agentcore_control.types.listing_mode.serialize_json(
                value["listing_mode"]
            )
        )
    if "resource_priority" in value:
        out["resourcePriority"] = value["resource_priority"]
    return out


def deserialize_json(data: dict) -> McpServerTargetConfiguration:
    out: McpServerTargetConfiguration = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("McpServerTargetConfiguration.endpoint required")
    if "mcpToolSchema" in data:
        import capo_bedrock_agentcore_control.types.mcp_tool_schema_configuration

        out["mcp_tool_schema"] = (
            capo_bedrock_agentcore_control.types.mcp_tool_schema_configuration.deserialize_json(
                data["mcpToolSchema"]
            )
        )
    if "listingMode" in data:
        import capo_bedrock_agentcore_control.types.listing_mode

        out["listing_mode"] = (
            capo_bedrock_agentcore_control.types.listing_mode.deserialize_json(
                data["listingMode"]
            )
        )
    if "resourcePriority" in data:
        out["resource_priority"] = data["resourcePriority"]
    return out
