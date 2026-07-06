"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DisableDNSViewOutput``."""

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


class DisableDNSViewOutput(TypedDict, closed=True):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the disabled DNS view.</p>"""
    arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the disabled DNS view.</p>"""
    client_token: NotRequired[
        "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    dnssec_validation: "aws_sdk_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
    """<p>Whether DNSSEC validation is enabled for the disabled DNS view.</p>"""
    edns_client_subnet: "aws_sdk_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
    """<p>Whether EDNS Client Subnet injection is enabled for the disabled DNS view.</p>"""
    firewall_rules_fail_open: "aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
    """<p>The firewall rules fail-open behavior configured for the disabled DNS view.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the disabled DNS view.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the disabled DNS view.</p>"""
    global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver that the disabled DNS view is associated with.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the DNS view was originally created.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the DNS view was last updated.</p>"""
    status: "aws_sdk_route53globalresolver.types.profile_resource_status.ProfileResourceStatus"
    """<p>The current status of the disabled DNS view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableDNSViewOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "client_token" in value:
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


def deserialize_json(data: dict) -> DisableDNSViewOutput:
    out: DisableDNSViewOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DisableDNSViewOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DisableDNSViewOutput.arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "dnssecValidation" in data:
        import aws_sdk_route53globalresolver.types.dns_sec_validation_type

        out["dnssec_validation"] = (
            aws_sdk_route53globalresolver.types.dns_sec_validation_type.deserialize_json(
                data["dnssecValidation"]
            )
        )
    else:
        raise DeserializationError("DisableDNSViewOutput.dnssec_validation required")
    if "ednsClientSubnet" in data:
        import aws_sdk_route53globalresolver.types.edns_client_subnet_type

        out["edns_client_subnet"] = (
            aws_sdk_route53globalresolver.types.edns_client_subnet_type.deserialize_json(
                data["ednsClientSubnet"]
            )
        )
    else:
        raise DeserializationError("DisableDNSViewOutput.edns_client_subnet required")
    if "firewallRulesFailOpen" in data:
        import aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewall_rules_fail_open"] = (
            aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.deserialize_json(
                data["firewallRulesFailOpen"]
            )
        )
    else:
        raise DeserializationError(
            "DisableDNSViewOutput.firewall_rules_fail_open required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DisableDNSViewOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "globalResolverId" in data:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        raise DeserializationError("DisableDNSViewOutput.global_resolver_id required")
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DisableDNSViewOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DisableDNSViewOutput.updated_at required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.profile_resource_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.profile_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DisableDNSViewOutput.status required")
    return out
