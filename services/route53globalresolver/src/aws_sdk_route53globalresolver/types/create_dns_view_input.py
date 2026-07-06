"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateDNSViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.dns_sec_validation_type
    import aws_sdk_route53globalresolver.types.edns_client_subnet_type
    import aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name
    import aws_sdk_route53globalresolver.types.tags


class CreateDNSViewInput(TypedDict, closed=True):
    global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver to associate with this DNS view.</p>"""
    client_token: NotRequired[
        "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique string that identifies the request and ensures idempotency.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>A descriptive name for the DNS view.</p>"""
    dnssec_validation: "aws_sdk_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
    """<p>Whether to enable DNSSEC validation for DNS queries in this DNS view. When enabled, the resolver verifies the authenticity and integrity of DNS responses from public name servers for DNSSEC-signed domains.</p>"""
    edns_client_subnet: "aws_sdk_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
    """<p>Whether to enable EDNS Client Subnet injection for DNS queries in this DNS view. When enabled, client subnet information is forwarded to provide more accurate geographic-based DNS responses.</p>"""
    firewall_rules_fail_open: "aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
    """<p>Determines the behavior when Route 53 Global Resolver cannot apply DNS firewall rules due to service impairment. When enabled, DNS queries are allowed through; when disabled, queries are blocked.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description for the DNS view.</p>"""
    tags: NotRequired["aws_sdk_route53globalresolver.types.tags.Tags"]
    """<p>Tags to associate with the DNS view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDNSViewInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    import aws_sdk_route53globalresolver.types.dns_sec_validation_type

    out["dnssecValidation"] = (
        aws_sdk_route53globalresolver.types.dns_sec_validation_type.serialize_json(
            value.get("dnssec_validation", "DISABLED")
        )
    )
    import aws_sdk_route53globalresolver.types.edns_client_subnet_type

    out["ednsClientSubnet"] = (
        aws_sdk_route53globalresolver.types.edns_client_subnet_type.serialize_json(
            value.get("edns_client_subnet", "DISABLED")
        )
    )
    import aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type

    out["firewallRulesFailOpen"] = (
        aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.serialize_json(
            value.get("firewall_rules_fail_open", "DISABLED")
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDNSViewInput:
    out: CreateDNSViewInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDNSViewInput.name required")
    if "dnssecValidation" in data:
        import aws_sdk_route53globalresolver.types.dns_sec_validation_type

        out["dnssec_validation"] = (
            aws_sdk_route53globalresolver.types.dns_sec_validation_type.deserialize_json(
                data["dnssecValidation"]
            )
        )
    else:
        out["dnssec_validation"] = "DISABLED"
    if "ednsClientSubnet" in data:
        import aws_sdk_route53globalresolver.types.edns_client_subnet_type

        out["edns_client_subnet"] = (
            aws_sdk_route53globalresolver.types.edns_client_subnet_type.deserialize_json(
                data["ednsClientSubnet"]
            )
        )
    else:
        out["edns_client_subnet"] = "DISABLED"
    if "firewallRulesFailOpen" in data:
        import aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewall_rules_fail_open"] = (
            aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.deserialize_json(
                data["firewallRulesFailOpen"]
            )
        )
    else:
        out["firewall_rules_fail_open"] = "DISABLED"
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.deserialize_json(
            data["tags"]
        )
    return out
