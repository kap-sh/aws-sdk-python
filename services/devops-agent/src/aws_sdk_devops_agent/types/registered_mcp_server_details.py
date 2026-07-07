"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredMCPServerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.description
    import aws_sdk_devops_agent.types.mcp_server_authorization_method


class RegisteredMCPServerDetails(TypedDict, closed=True):
    name: "str"
    """<p>The MCP server name.</p>"""
    endpoint: "str"
    """<p>The MCP server endpoint URL.</p>"""
    authorization_method: "aws_sdk_devops_agent.types.mcp_server_authorization_method.MCPServerAuthorizationMethod"
    """<p>The MCP server uses this authorization method.</p>"""
    description: NotRequired["aws_sdk_devops_agent.types.description.Description"]
    """<p>Optional description for the MCP server.</p>"""
    api_key_header: NotRequired["str"]
    """<p>If the MCP server uses API key authentication, these details are provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredMCPServerDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["endpoint"] = value["endpoint"]
    import aws_sdk_devops_agent.types.mcp_server_authorization_method

    out["authorizationMethod"] = (
        aws_sdk_devops_agent.types.mcp_server_authorization_method.serialize_json(
            value["authorization_method"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "api_key_header" in value:
        out["apiKeyHeader"] = value["api_key_header"]
    return out


def deserialize_json(data: dict) -> RegisteredMCPServerDetails:
    out: RegisteredMCPServerDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegisteredMCPServerDetails.name required")
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("RegisteredMCPServerDetails.endpoint required")
    if "authorizationMethod" in data:
        import aws_sdk_devops_agent.types.mcp_server_authorization_method

        out["authorization_method"] = (
            aws_sdk_devops_agent.types.mcp_server_authorization_method.deserialize_json(
                data["authorizationMethod"]
            )
        )
    else:
        raise DeserializationError(
            "RegisteredMCPServerDetails.authorization_method required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "apiKeyHeader" in data:
        out["api_key_header"] = data["apiKeyHeader"]
    return out
