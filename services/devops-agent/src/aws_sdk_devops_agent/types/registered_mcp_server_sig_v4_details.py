"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredMCPServerSigV4Details``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.custom_headers
    import aws_sdk_devops_agent.types.description
    import aws_sdk_devops_agent.types.mcp_server_endpoint
    import aws_sdk_devops_agent.types.mcp_server_name
    import aws_sdk_devops_agent.types.role_arn
    import aws_sdk_devops_agent.types.sig_v4_region


class RegisteredMCPServerSigV4Details(TypedDict, closed=True):
    name: "aws_sdk_devops_agent.types.mcp_server_name.MCPServerName"
    """<p>MCP server name.</p>"""
    endpoint: "aws_sdk_devops_agent.types.mcp_server_endpoint.MCPServerEndpoint"
    """<p>MCP server endpoint URL.</p>"""
    description: NotRequired["aws_sdk_devops_agent.types.description.Description"]
    """<p>Optional description for the MCP server.</p>"""
    region: "aws_sdk_devops_agent.types.sig_v4_region.SigV4Region"
    """<p>AWS region for SigV4 signing. Use '*' for SigV4a multi-region signing.</p>"""
    service: "str"
    """<p>AWS service name for SigV4 signing.</p>"""
    role_arn: "str"
    """<p>IAM role ARN to assume for SigV4 signing.</p>"""
    mcp_role_arn: NotRequired["aws_sdk_devops_agent.types.role_arn.RoleArn"]
    custom_headers: NotRequired[
        "aws_sdk_devops_agent.types.custom_headers.CustomHeaders"
    ]
    """<p>Custom headers for the SigV4 MCP server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredMCPServerSigV4Details) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["endpoint"] = value["endpoint"]
    if "description" in value:
        out["description"] = value["description"]
    out["region"] = value["region"]
    out["service"] = value["service"]
    out["roleArn"] = value.get("role_arn", "")
    if "mcp_role_arn" in value:
        out["mcpRoleArn"] = value["mcp_role_arn"]
    if "custom_headers" in value:
        import aws_sdk_devops_agent.types.custom_headers

        out["customHeaders"] = aws_sdk_devops_agent.types.custom_headers.serialize_json(
            value["custom_headers"]
        )
    return out


def deserialize_json(data: dict) -> RegisteredMCPServerSigV4Details:
    out: RegisteredMCPServerSigV4Details = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegisteredMCPServerSigV4Details.name required")
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("RegisteredMCPServerSigV4Details.endpoint required")
    if "description" in data:
        out["description"] = data["description"]
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("RegisteredMCPServerSigV4Details.region required")
    if "service" in data:
        out["service"] = data["service"]
    else:
        raise DeserializationError("RegisteredMCPServerSigV4Details.service required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if "mcpRoleArn" in data:
        out["mcp_role_arn"] = data["mcpRoleArn"]
    if "customHeaders" in data:
        import aws_sdk_devops_agent.types.custom_headers

        out["custom_headers"] = (
            aws_sdk_devops_agent.types.custom_headers.deserialize_json(
                data["customHeaders"]
            )
        )
    return out
