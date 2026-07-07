"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateFirewallDomainsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.domains
    import aws_sdk_route53globalresolver.types.resource_id


class UpdateFirewallDomainsInput(TypedDict, closed=True):
    domains: "aws_sdk_route53globalresolver.types.domains.Domains"
    """<p>A list of the domains. You can add up to 1000 domains per request.</p>"""
    firewall_domain_list_id: (
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    )
    """<p>The ID of the DNS Firewall domain list to which you want to add the domains.</p>"""
    operation: "str"
    """<p>The operation for updating the domain list. The allowed values are ADD, REMOVE, and REPLACE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFirewallDomainsInput) -> dict:
    out: dict = {}
    import aws_sdk_route53globalresolver.types.domains

    out["domains"] = aws_sdk_route53globalresolver.types.domains.serialize_json(
        value["domains"]
    )
    out["operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> UpdateFirewallDomainsInput:
    out: UpdateFirewallDomainsInput = {}  # type: ignore[typeddict-item]
    if "domains" in data:
        import aws_sdk_route53globalresolver.types.domains

        out["domains"] = aws_sdk_route53globalresolver.types.domains.deserialize_json(
            data["domains"]
        )
    else:
        raise DeserializationError("UpdateFirewallDomainsInput.domains required")
    if "operation" in data:
        out["operation"] = data["operation"]
    else:
        raise DeserializationError("UpdateFirewallDomainsInput.operation required")
    return out
