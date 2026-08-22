"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProxyBypass``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.domain_patterns


class ProxyBypass(TypedDict, closed=True):
    domain_patterns: NotRequired[
        "capo_bedrock_agentcore.types.domain_patterns.DomainPatterns"
    ]
    """<p>Array of domain patterns that should bypass the proxy. Supports <code>.amazonaws.com</code> for subdomain matching or <code>amazonaws.com</code> for exact domain matching. Requests to these domains connect directly without using any proxy. Maximum 253 characters per pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProxyBypass) -> dict:
    out: dict = {}
    if "domain_patterns" in value:
        import capo_bedrock_agentcore.types.domain_patterns

        out["domainPatterns"] = (
            capo_bedrock_agentcore.types.domain_patterns.serialize_json(
                value["domain_patterns"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProxyBypass:
    out: ProxyBypass = {}  # type: ignore[typeddict-item]
    if data.get("domainPatterns") is not None:
        import capo_bedrock_agentcore.types.domain_patterns

        out["domain_patterns"] = (
            capo_bedrock_agentcore.types.domain_patterns.deserialize_json(
                data["domainPatterns"]
            )
        )
    return out
