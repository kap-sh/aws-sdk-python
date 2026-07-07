"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DNSViewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.dns_sec_validation_type
    import aws_sdk_route53globalresolver.types.edns_client_subnet_type
    import aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.profile_resource_status
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class DNSViewSummary(TypedDict, closed=True):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the DNS view.</p>"""
    arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the DNS view.</p>"""
    client_token: "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    dnssec_validation: "aws_sdk_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
    """<p>Whether DNSSEC validation is enabled for the DNS view.</p>"""
    edns_client_subnet: "aws_sdk_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
    """<p>Whether EDNS Client Subnet injection is enabled for the DNS view.</p>"""
    firewall_rules_fail_open: "aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
    """<p>Whether firewall rules fail open when they cannot be evaluated.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the DNS view.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the DNS view.</p>"""
    global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the global resolver that the DNS view is associated with.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the DNS view was created.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the DNS view was last updated.</p>"""
    status: "aws_sdk_route53globalresolver.types.profile_resource_status.ProfileResourceStatus"
    """<p>The current status of the DNS view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DNSViewSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["clientToken"] = value["client_token"]
    import aws_sdk_route53globalresolver.types.dns_sec_validation_type

    out["dnssecValidation"] = (
        aws_sdk_route53globalresolver.types.dns_sec_validation_type.serialize_json(
            value["dnssec_validation"]
        )
    )
    import aws_sdk_route53globalresolver.types.edns_client_subnet_type

    out["ednsClientSubnet"] = (
        aws_sdk_route53globalresolver.types.edns_client_subnet_type.serialize_json(
            value["edns_client_subnet"]
        )
    )
    import aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type

    out["firewallRulesFailOpen"] = (
        aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.serialize_json(
            value["firewall_rules_fail_open"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["globalResolverId"] = value["global_resolver_id"]
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    import aws_sdk_route53globalresolver.types.profile_resource_status

    out["status"] = (
        aws_sdk_route53globalresolver.types.profile_resource_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DNSViewSummary:
    out: DNSViewSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DNSViewSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DNSViewSummary.arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("DNSViewSummary.client_token required")
    if "dnssecValidation" in data:
        import aws_sdk_route53globalresolver.types.dns_sec_validation_type

        out["dnssec_validation"] = (
            aws_sdk_route53globalresolver.types.dns_sec_validation_type.deserialize_json(
                data["dnssecValidation"]
            )
        )
    else:
        raise DeserializationError("DNSViewSummary.dnssec_validation required")
    if "ednsClientSubnet" in data:
        import aws_sdk_route53globalresolver.types.edns_client_subnet_type

        out["edns_client_subnet"] = (
            aws_sdk_route53globalresolver.types.edns_client_subnet_type.deserialize_json(
                data["ednsClientSubnet"]
            )
        )
    else:
        raise DeserializationError("DNSViewSummary.edns_client_subnet required")
    if "firewallRulesFailOpen" in data:
        import aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewall_rules_fail_open"] = (
            aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.deserialize_json(
                data["firewallRulesFailOpen"]
            )
        )
    else:
        raise DeserializationError("DNSViewSummary.firewall_rules_fail_open required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DNSViewSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "globalResolverId" in data:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        raise DeserializationError("DNSViewSummary.global_resolver_id required")
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DNSViewSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DNSViewSummary.updated_at required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.profile_resource_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.profile_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DNSViewSummary.status required")
    return out
