"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetGlobalResolverOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.global_resolver_ip_address_type
    import capo_route53globalresolver.types.i_pv4_addresses
    import capo_route53globalresolver.types.i_pv6_addresses
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.region
    import capo_route53globalresolver.types.regions
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.sni


class GetGlobalResolverOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Global Resolver.</p>"""
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Global Resolver.</p>"""
    client_token: "capo_route53globalresolver.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>"""
    dns_name: "capo_route53globalresolver.types.sni.Sni"
    """<p>The hostname used by the customers' DNS clients for certification validation.</p>"""
    observability_region: NotRequired["capo_route53globalresolver.types.region.Region"]
    """<p>The Amazon Web Services Regions in which the users' Global Resolver query resolution logs will be propagated.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the Global Resolver.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the Global Resolver.</p>"""
    regions: "capo_route53globalresolver.types.regions.Regions"
    """<p>The Amazon Web Services Regions in which the Global Resolver operate.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time the Global Resolver was created.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time the Global Resolver was updated.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The operational status of the Global Resolver.</p>"""
    ipv4_addresses: "capo_route53globalresolver.types.i_pv4_addresses.IPv4Addresses"
    """<p>List of anycast IPv4 addresses associated with the Global Resolver instance.</p>"""
    ipv6_addresses: NotRequired[
        "capo_route53globalresolver.types.i_pv6_addresses.IPv6Addresses"
    ]
    """<p>List of anycast IPv6 addresses associated with the Global Resolver instance. This field is only populated when ipAddressType is DUAL_STACK.</p>"""
    ip_address_type: NotRequired[
        "capo_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
    ]
    """<p>The IP address type configured for the Global Resolver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlobalResolverOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["clientToken"] = value["client_token"]
    out["dnsName"] = value["dns_name"]
    if "observability_region" in value:
        out["observabilityRegion"] = value["observability_region"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_route53globalresolver.types.regions

    out["regions"] = capo_route53globalresolver.types.regions.serialize_json(
        value["regions"]
    )
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
    import capo_route53globalresolver.types.cr_resource_status

    out["status"] = capo_route53globalresolver.types.cr_resource_status.serialize_json(
        value["status"]
    )
    import capo_route53globalresolver.types.i_pv4_addresses

    out["ipv4Addresses"] = (
        capo_route53globalresolver.types.i_pv4_addresses.serialize_json(
            value["ipv4_addresses"]
        )
    )
    if "ipv6_addresses" in value:
        import capo_route53globalresolver.types.i_pv6_addresses

        out["ipv6Addresses"] = (
            capo_route53globalresolver.types.i_pv6_addresses.serialize_json(
                value["ipv6_addresses"]
            )
        )
    if "ip_address_type" in value:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ipAddressType"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGlobalResolverOutput:
    out: GetGlobalResolverOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetGlobalResolverOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetGlobalResolverOutput.arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("GetGlobalResolverOutput.client_token required")
    if "dnsName" in data:
        out["dns_name"] = data["dnsName"]
    else:
        raise DeserializationError("GetGlobalResolverOutput.dns_name required")
    if "observabilityRegion" in data:
        out["observability_region"] = data["observabilityRegion"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetGlobalResolverOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "regions" in data:
        import capo_route53globalresolver.types.regions

        out["regions"] = capo_route53globalresolver.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("GetGlobalResolverOutput.regions required")
    if "createdAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetGlobalResolverOutput.created_at required")
    if "updatedAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetGlobalResolverOutput.updated_at required")
    if "status" in data:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetGlobalResolverOutput.status required")
    if "ipv4Addresses" in data:
        import capo_route53globalresolver.types.i_pv4_addresses

        out["ipv4_addresses"] = (
            capo_route53globalresolver.types.i_pv4_addresses.deserialize_json(
                data["ipv4Addresses"]
            )
        )
    else:
        raise DeserializationError("GetGlobalResolverOutput.ipv4_addresses required")
    if "ipv6Addresses" in data:
        import capo_route53globalresolver.types.i_pv6_addresses

        out["ipv6_addresses"] = (
            capo_route53globalresolver.types.i_pv6_addresses.deserialize_json(
                data["ipv6Addresses"]
            )
        )
    if "ipAddressType" in data:
        import capo_route53globalresolver.types.global_resolver_ip_address_type

        out["ip_address_type"] = (
            capo_route53globalresolver.types.global_resolver_ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    return out
