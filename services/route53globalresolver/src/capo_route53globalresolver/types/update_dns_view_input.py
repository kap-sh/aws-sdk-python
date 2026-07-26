"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateDNSViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.dns_sec_validation_type
    import capo_route53globalresolver.types.edns_client_subnet_type
    import capo_route53globalresolver.types.firewall_rules_fail_open_type
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class UpdateDNSViewInput(TypedDict, closed=True):
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the DNS view to update.</p>"""
    name: NotRequired["capo_route53globalresolver.types.resource_name.ResourceName"]
    """<p>The name of the DNS view.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the DNS view.</p>"""
    dnssec_validation: NotRequired[
        "capo_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
    ]
    """<p>Whether to enable DNSSEC validation for the DNS view.</p>"""
    edns_client_subnet: NotRequired[
        "capo_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
    ]
    """<p>Whether to enable EDNS Client Subnet injection for the DNS view.</p>"""
    firewall_rules_fail_open: NotRequired[
        "capo_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
    ]
    """<p>Whether firewall rules should fail open when they cannot be evaluated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDNSViewInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "dnssec_validation" in value:
        import capo_route53globalresolver.types.dns_sec_validation_type

        out["dnssecValidation"] = (
            capo_route53globalresolver.types.dns_sec_validation_type.serialize_json(
                value["dnssec_validation"]
            )
        )
    if "edns_client_subnet" in value:
        import capo_route53globalresolver.types.edns_client_subnet_type

        out["ednsClientSubnet"] = (
            capo_route53globalresolver.types.edns_client_subnet_type.serialize_json(
                value["edns_client_subnet"]
            )
        )
    if "firewall_rules_fail_open" in value:
        import capo_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewallRulesFailOpen"] = (
            capo_route53globalresolver.types.firewall_rules_fail_open_type.serialize_json(
                value["firewall_rules_fail_open"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDNSViewInput:
    out: UpdateDNSViewInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "dnssecValidation" in data:
        import capo_route53globalresolver.types.dns_sec_validation_type

        out["dnssec_validation"] = (
            capo_route53globalresolver.types.dns_sec_validation_type.deserialize_json(
                data["dnssecValidation"]
            )
        )
    if "ednsClientSubnet" in data:
        import capo_route53globalresolver.types.edns_client_subnet_type

        out["edns_client_subnet"] = (
            capo_route53globalresolver.types.edns_client_subnet_type.deserialize_json(
                data["ednsClientSubnet"]
            )
        )
    if "firewallRulesFailOpen" in data:
        import capo_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewall_rules_fail_open"] = (
            capo_route53globalresolver.types.firewall_rules_fail_open_type.deserialize_json(
                data["firewallRulesFailOpen"]
            )
        )
    return out
