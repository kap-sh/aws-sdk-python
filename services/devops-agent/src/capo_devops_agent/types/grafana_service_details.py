"""Generated from Smithy shape ``com.amazonaws.devopsagent#GrafanaServiceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.description
    import capo_devops_agent.types.mcp_server_authorization_config
    import capo_devops_agent.types.mcp_server_endpoint
    import capo_devops_agent.types.mcp_server_name


class GrafanaServiceDetails(TypedDict, closed=True):
    name: "capo_devops_agent.types.mcp_server_name.MCPServerName"
    """<p>MCP server name.</p>"""
    endpoint: "capo_devops_agent.types.mcp_server_endpoint.MCPServerEndpoint"
    """<p>MCP server endpoint URL.</p>"""
    description: NotRequired["capo_devops_agent.types.description.Description"]
    """<p>Optional description for the MCP server.</p>"""
    authorization_config: "capo_devops_agent.types.mcp_server_authorization_config.MCPServerAuthorizationConfig"
    """<p>Grafana MCP server authorization configuration (experimental).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrafanaServiceDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["endpoint"] = value["endpoint"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_devops_agent.types.mcp_server_authorization_config

    out["authorizationConfig"] = (
        capo_devops_agent.types.mcp_server_authorization_config.serialize_json(
            value["authorization_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> GrafanaServiceDetails:
    out: GrafanaServiceDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GrafanaServiceDetails.name required")
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("GrafanaServiceDetails.endpoint required")
    if "description" in data:
        out["description"] = data["description"]
    if "authorizationConfig" in data:
        import capo_devops_agent.types.mcp_server_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.mcp_server_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GrafanaServiceDetails.authorization_config required"
        )
    return out
