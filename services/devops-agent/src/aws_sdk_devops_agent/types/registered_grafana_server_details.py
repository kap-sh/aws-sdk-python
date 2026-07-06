"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredGrafanaServerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.mcp_server_authorization_method
    import aws_sdk_devops_agent.types.mcp_server_endpoint


class RegisteredGrafanaServerDetails(TypedDict, closed=True):
    endpoint: "aws_sdk_devops_agent.types.mcp_server_endpoint.MCPServerEndpoint"
    """<p>Grafana instance URL (e.g., https://your-instance.grafana.net)</p>"""
    authorization_method: "aws_sdk_devops_agent.types.mcp_server_authorization_method.MCPServerAuthorizationMethod"
    """<p>The authz method used by the MCP server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredGrafanaServerDetails) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    import aws_sdk_devops_agent.types.mcp_server_authorization_method

    out["authorizationMethod"] = (
        aws_sdk_devops_agent.types.mcp_server_authorization_method.serialize_json(
            value["authorization_method"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegisteredGrafanaServerDetails:
    out: RegisteredGrafanaServerDetails = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("RegisteredGrafanaServerDetails.endpoint required")
    if "authorizationMethod" in data:
        import aws_sdk_devops_agent.types.mcp_server_authorization_method

        out["authorization_method"] = (
            aws_sdk_devops_agent.types.mcp_server_authorization_method.deserialize_json(
                data["authorizationMethod"]
            )
        )
    else:
        raise DeserializationError(
            "RegisteredGrafanaServerDetails.authorization_method required"
        )
    return out
