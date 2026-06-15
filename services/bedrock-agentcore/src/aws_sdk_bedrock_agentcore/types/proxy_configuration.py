"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProxyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.proxies
    import aws_sdk_bedrock_agentcore.types.proxy_bypass


class ProxyConfiguration(TypedDict):
    proxies: "aws_sdk_bedrock_agentcore.types.proxies.Proxies"
    """<p>An array of 1-5 proxy server configurations for domain-based routing. Each proxy can specify which domains it handles via <code>domainPatterns</code>, enabling flexible routing of different traffic through different proxies based on destination domain.</p>"""
    bypass: NotRequired["aws_sdk_bedrock_agentcore.types.proxy_bypass.ProxyBypass"]
    """<p>Optional configuration for domains that should bypass all proxies and connect directly to their destination, like the internet. Takes precedence over all proxy routing rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProxyConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.proxies

    out["proxies"] = aws_sdk_bedrock_agentcore.types.proxies.serialize_json(
        value["proxies"]
    )
    if "bypass" in value:
        import aws_sdk_bedrock_agentcore.types.proxy_bypass

        out["bypass"] = aws_sdk_bedrock_agentcore.types.proxy_bypass.serialize_json(
            value["bypass"]
        )
    return out


def deserialize_json(data: dict) -> ProxyConfiguration:
    out: ProxyConfiguration = {}  # type: ignore[typeddict-item]
    if "proxies" in data:
        import aws_sdk_bedrock_agentcore.types.proxies

        out["proxies"] = aws_sdk_bedrock_agentcore.types.proxies.deserialize_json(
            data["proxies"]
        )
    else:
        raise DeserializationError("ProxyConfiguration.proxies required")
    if "bypass" in data:
        import aws_sdk_bedrock_agentcore.types.proxy_bypass

        out["bypass"] = aws_sdk_bedrock_agentcore.types.proxy_bypass.deserialize_json(
            data["bypass"]
        )
    return out
