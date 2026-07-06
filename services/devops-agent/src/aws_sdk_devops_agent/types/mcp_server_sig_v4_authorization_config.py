"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerSigV4AuthorizationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.custom_headers
    import aws_sdk_devops_agent.types.role_arn
    import aws_sdk_devops_agent.types.sig_v4_region


class MCPServerSigV4AuthorizationConfig(TypedDict, closed=True):
    region: "aws_sdk_devops_agent.types.sig_v4_region.SigV4Region"
    """<p>AWS region for SigV4 signing. Use '*' for SigV4a multi-region signing.</p>"""
    service: "str"
    """<p>AWS service name for SigV4 signing.</p>"""
    role_arn: "str"
    """<p>Deprecated — use mcpRoleArn instead. IAM role ARN to assume for SigV4 signing.</p>"""
    mcp_role_arn: NotRequired["aws_sdk_devops_agent.types.role_arn.RoleArn"]
    """<p>IAM role ARN to assume for SigV4 signing. Optional — when omitted, credentials are resolved at runtime via a monitor account association.</p>"""
    custom_headers: NotRequired[
        "aws_sdk_devops_agent.types.custom_headers.CustomHeaders"
    ]
    """<p>Custom headers for the SigV4 MCP server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerSigV4AuthorizationConfig) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> MCPServerSigV4AuthorizationConfig:
    out: MCPServerSigV4AuthorizationConfig = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("MCPServerSigV4AuthorizationConfig.region required")
    if "service" in data:
        out["service"] = data["service"]
    else:
        raise DeserializationError("MCPServerSigV4AuthorizationConfig.service required")
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
