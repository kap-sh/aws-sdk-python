"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteDNSViewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.dns_sec_validation_type
    import capo_route53globalresolver.types.edns_client_subnet_type
    import capo_route53globalresolver.types.firewall_rules_fail_open_type
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.profile_resource_status
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class DeleteDNSViewOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted DNS view.</p>"""
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the deleted DNS view.</p>"""
    client_token: NotRequired[
        "capo_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    dnssec_validation: (
        "capo_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
    )
    """<p>Whether DNSSEC validation was enabled for the deleted DNS view.</p>"""
    edns_client_subnet: (
        "capo_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
    )
    """<p>Whether EDNS Client Subnet injection was enabled for the deleted DNS view.</p>"""
    firewall_rules_fail_open: "capo_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
    """<p>The firewall rules fail-open behavior that was configured for the deleted DNS view.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the deleted DNS view.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the deleted DNS view.</p>"""
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver that the deleted DNS view was associated with.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the DNS view was originally created.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the DNS view was last updated before deletion.</p>"""
    status: (
        "capo_route53globalresolver.types.profile_resource_status.ProfileResourceStatus"
    )
    """<p>The final status of the deleted DNS view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDNSViewOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_route53globalresolver.types.dns_sec_validation_type

    out["dnssecValidation"] = (
        capo_route53globalresolver.types.dns_sec_validation_type.serialize_json(
            value["dnssec_validation"]
        )
    )
    import capo_route53globalresolver.types.edns_client_subnet_type

    out["ednsClientSubnet"] = (
        capo_route53globalresolver.types.edns_client_subnet_type.serialize_json(
            value["edns_client_subnet"]
        )
    )
    import capo_route53globalresolver.types.firewall_rules_fail_open_type

    out["firewallRulesFailOpen"] = (
        capo_route53globalresolver.types.firewall_rules_fail_open_type.serialize_json(
            value["firewall_rules_fail_open"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["globalResolverId"] = value["global_resolver_id"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    import capo_route53globalresolver.types.profile_resource_status

    out["status"] = (
        capo_route53globalresolver.types.profile_resource_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteDNSViewOutput:
    out: DeleteDNSViewOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteDNSViewOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteDNSViewOutput.arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "dnssecValidation" in data:
        import capo_route53globalresolver.types.dns_sec_validation_type

        out["dnssec_validation"] = (
            capo_route53globalresolver.types.dns_sec_validation_type.deserialize_json(
                data["dnssecValidation"]
            )
        )
    else:
        raise DeserializationError("DeleteDNSViewOutput.dnssec_validation required")
    if "ednsClientSubnet" in data:
        import capo_route53globalresolver.types.edns_client_subnet_type

        out["edns_client_subnet"] = (
            capo_route53globalresolver.types.edns_client_subnet_type.deserialize_json(
                data["ednsClientSubnet"]
            )
        )
    else:
        raise DeserializationError("DeleteDNSViewOutput.edns_client_subnet required")
    if "firewallRulesFailOpen" in data:
        import capo_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewall_rules_fail_open"] = (
            capo_route53globalresolver.types.firewall_rules_fail_open_type.deserialize_json(
                data["firewallRulesFailOpen"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteDNSViewOutput.firewall_rules_fail_open required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteDNSViewOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "globalResolverId" in data:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        raise DeserializationError("DeleteDNSViewOutput.global_resolver_id required")
    if "createdAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DeleteDNSViewOutput.created_at required")
    if "updatedAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DeleteDNSViewOutput.updated_at required")
    if "status" in data:
        import capo_route53globalresolver.types.profile_resource_status

        out["status"] = (
            capo_route53globalresolver.types.profile_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteDNSViewOutput.status required")
    return out
