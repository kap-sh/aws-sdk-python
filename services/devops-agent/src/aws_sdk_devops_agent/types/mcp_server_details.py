"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.description
    import aws_sdk_devops_agent.types.mcp_server_authorization_config
    import aws_sdk_devops_agent.types.mcp_server_endpoint
    import aws_sdk_devops_agent.types.mcp_server_name


class MCPServerDetails(TypedDict, closed=True):
    name: "aws_sdk_devops_agent.types.mcp_server_name.MCPServerName"
    """<p>MCP server name.</p>"""
    endpoint: "aws_sdk_devops_agent.types.mcp_server_endpoint.MCPServerEndpoint"
    """<p>MCP server endpoint URL.</p>"""
    description: NotRequired["aws_sdk_devops_agent.types.description.Description"]
    """<p>Optional description for the MCP server.</p>"""
    authorization_config: "aws_sdk_devops_agent.types.mcp_server_authorization_config.MCPServerAuthorizationConfig"
    """<p>MCP server authorization configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["endpoint"] = value["endpoint"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_devops_agent.types.mcp_server_authorization_config

    out["authorizationConfig"] = (
        aws_sdk_devops_agent.types.mcp_server_authorization_config.serialize_json(
            value["authorization_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> MCPServerDetails:
    out: MCPServerDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MCPServerDetails.name required")
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("MCPServerDetails.endpoint required")
    if "description" in data:
        out["description"] = data["description"]
    if "authorizationConfig" in data:
        import aws_sdk_devops_agent.types.mcp_server_authorization_config

        out["authorization_config"] = (
            aws_sdk_devops_agent.types.mcp_server_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    else:
        raise DeserializationError("MCPServerDetails.authorization_config required")
    return out
