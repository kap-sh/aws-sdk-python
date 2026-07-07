"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerGrafanaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.mcp_tools_list


class MCPServerGrafanaConfiguration(TypedDict, closed=True):
    endpoint: "str"
    """<p>Grafana instance URL (e.g., https://your-instance.grafana.net)</p>"""
    organization_id: NotRequired["str"]
    """<p>The Grafana organization ID that can be used.</p>"""
    tools: NotRequired["aws_sdk_devops_agent.types.mcp_tools_list.MCPToolsList"]
    """<p>List of MCP tools that can be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerGrafanaConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    if "tools" in value:
        import aws_sdk_devops_agent.types.mcp_tools_list

        out["tools"] = aws_sdk_devops_agent.types.mcp_tools_list.serialize_json(
            value["tools"]
        )
    return out


def deserialize_json(data: dict) -> MCPServerGrafanaConfiguration:
    out: MCPServerGrafanaConfiguration = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("MCPServerGrafanaConfiguration.endpoint required")
    if "organizationId" in data:
        out["organization_id"] = data["organizationId"]
    if "tools" in data:
        import aws_sdk_devops_agent.types.mcp_tools_list

        out["tools"] = aws_sdk_devops_agent.types.mcp_tools_list.deserialize_json(
            data["tools"]
        )
    return out
