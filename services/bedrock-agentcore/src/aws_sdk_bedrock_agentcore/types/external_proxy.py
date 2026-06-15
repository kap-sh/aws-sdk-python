"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExternalProxy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.domain_patterns
    import aws_sdk_bedrock_agentcore.types.host_name
    import aws_sdk_bedrock_agentcore.types.proxy_credentials


class ExternalProxy(TypedDict):
    server: "aws_sdk_bedrock_agentcore.types.host_name.HostName"
    """<p>The hostname of the proxy server. Must be a valid DNS hostname (maximum 253 characters).</p>"""
    port: "int"
    """<p>The port number of the proxy server. Valid range: 1-65535.</p>"""
    domain_patterns: NotRequired[
        "aws_sdk_bedrock_agentcore.types.domain_patterns.DomainPatterns"
    ]
    """<p>Optional array of domain patterns that should route through this specific proxy. Supports <code>.example.com</code> for subdomain matching (matches any subdomain of example.com) or <code>example.com</code> for exact domain matching. If omitted, this proxy acts as a catch-all for domains not matched by other proxies. Maximum 100 patterns per proxy, each up to 253 characters.</p>"""
    credentials: NotRequired[
        "aws_sdk_bedrock_agentcore.types.proxy_credentials.ProxyCredentials"
    ]
    """<p>Optional authentication credentials for the proxy server. If omitted, the proxy is accessed without authentication (useful for IP-allowlisted proxies).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalProxy) -> dict:
    out: dict = {}
    out["server"] = value["server"]
    out["port"] = value["port"]
    if "domain_patterns" in value:
        import aws_sdk_bedrock_agentcore.types.domain_patterns

        out["domainPatterns"] = (
            aws_sdk_bedrock_agentcore.types.domain_patterns.serialize_json(
                value["domain_patterns"]
            )
        )
    if "credentials" in value:
        import aws_sdk_bedrock_agentcore.types.proxy_credentials

        out["credentials"] = (
            aws_sdk_bedrock_agentcore.types.proxy_credentials.serialize_json(
                value["credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExternalProxy:
    out: ExternalProxy = {}  # type: ignore[typeddict-item]
    if "server" in data:
        out["server"] = data["server"]
    else:
        raise DeserializationError("ExternalProxy.server required")
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("ExternalProxy.port required")
    if "domainPatterns" in data:
        import aws_sdk_bedrock_agentcore.types.domain_patterns

        out["domain_patterns"] = (
            aws_sdk_bedrock_agentcore.types.domain_patterns.deserialize_json(
                data["domainPatterns"]
            )
        )
    if "credentials" in data:
        import aws_sdk_bedrock_agentcore.types.proxy_credentials

        out["credentials"] = (
            aws_sdk_bedrock_agentcore.types.proxy_credentials.deserialize_json(
                data["credentials"]
            )
        )
    return out
