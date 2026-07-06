"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateGlobalResolverOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.cr_resource_status
    import aws_sdk_route53globalresolver.types.global_resolver_ip_address_type
    import aws_sdk_route53globalresolver.types.i_pv4_addresses
    import aws_sdk_route53globalresolver.types.i_pv6_addresses
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.region
    import aws_sdk_route53globalresolver.types.regions
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name
    import aws_sdk_route53globalresolver.types.sni


class CreateGlobalResolverOutput(TypedDict, closed=True):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier for the Route 53 Global Resolver.</p>"""
    arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Route 53 Global Resolver.</p>"""
    client_token: "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the Route 53 Global Resolver was created.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the Route 53 Global Resolver.</p>"""
    dns_name: "aws_sdk_route53globalresolver.types.sni.Sni"
    """<p>The hostname that DNS clients should use for TLS certificate validation when connecting to the Route 53 Global Resolver. This value resolves to the global anycast IP addresses for the resolver.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
    ]
    """<p>The IP address type configured for the Route 53 Global Resolver (IPV4 or DUAL_STACK).</p>"""
    ipv4_addresses: "aws_sdk_route53globalresolver.types.i_pv4_addresses.IPv4Addresses"
    """<p>The global anycast IPv4 addresses associated with the Route 53 Global Resolver. DNS clients can send queries to these addresses from anywhere on the internet.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_route53globalresolver.types.i_pv6_addresses.IPv6Addresses"
    ]
    """<p>The global anycast IPv6 addresses associated with the Route 53 Global Resolver. This field is only populated when ipAddressType is DUAL_STACK. DNS clients can send queries to these addresses from anywhere on the internet.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the Route 53 Global Resolver.</p>"""
    observability_region: NotRequired[
        "aws_sdk_route53globalresolver.types.region.Region"
    ]
    """<p>The Amazon Web Services Region where observability data for the Route 53 Global Resolver is stored.</p>"""
    regions: "aws_sdk_route53globalresolver.types.regions.Regions"
    """<p>The Amazon Web Services Regions where the Route 53 Global Resolver is deployed and operational.</p>"""
    status: "aws_sdk_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The current status of the Route 53 Global Resolver. Possible values are CREATING (being provisioned), UPDATING (being modified), OPERATIONAL (ready to serve queries), or DELETING (being removed).</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the Route 53 Global Resolver was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlobalResolverOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["clientToken"] = value["client_token"]
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    out["dnsName"] = value["dns_name"]
    if "ip_address_type" in value:
        import aws_sdk_route53globalresolver.types.global_resolver_ip_address_type

        out["ipAddressType"] = (
            aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    import aws_sdk_route53globalresolver.types.i_pv4_addresses

    out["ipv4Addresses"] = (
        aws_sdk_route53globalresolver.types.i_pv4_addresses.serialize_json(
            value["ipv4_addresses"]
        )
    )
    if "ipv6_addresses" in value:
        import aws_sdk_route53globalresolver.types.i_pv6_addresses

        out["ipv6Addresses"] = (
            aws_sdk_route53globalresolver.types.i_pv6_addresses.serialize_json(
                value["ipv6_addresses"]
            )
        )
    out["name"] = value["name"]
    if "observability_region" in value:
        out["observabilityRegion"] = value["observability_region"]
    import aws_sdk_route53globalresolver.types.regions

    out["regions"] = aws_sdk_route53globalresolver.types.regions.serialize_json(
        value["regions"]
    )
    import aws_sdk_route53globalresolver.types.cr_resource_status

    out["status"] = (
        aws_sdk_route53globalresolver.types.cr_resource_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateGlobalResolverOutput:
    out: CreateGlobalResolverOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateGlobalResolverOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateGlobalResolverOutput.arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateGlobalResolverOutput.client_token required")
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateGlobalResolverOutput.created_at required")
    if "description" in data:
        out["description"] = data["description"]
    if "dnsName" in data:
        out["dns_name"] = data["dnsName"]
    else:
        raise DeserializationError("CreateGlobalResolverOutput.dns_name required")
    if "ipAddressType" in data:
        import aws_sdk_route53globalresolver.types.global_resolver_ip_address_type

        out["ip_address_type"] = (
            aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if "ipv4Addresses" in data:
        import aws_sdk_route53globalresolver.types.i_pv4_addresses

        out["ipv4_addresses"] = (
            aws_sdk_route53globalresolver.types.i_pv4_addresses.deserialize_json(
                data["ipv4Addresses"]
            )
        )
    else:
        raise DeserializationError("CreateGlobalResolverOutput.ipv4_addresses required")
    if "ipv6Addresses" in data:
        import aws_sdk_route53globalresolver.types.i_pv6_addresses

        out["ipv6_addresses"] = (
            aws_sdk_route53globalresolver.types.i_pv6_addresses.deserialize_json(
                data["ipv6Addresses"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateGlobalResolverOutput.name required")
    if "observabilityRegion" in data:
        out["observability_region"] = data["observabilityRegion"]
    if "regions" in data:
        import aws_sdk_route53globalresolver.types.regions

        out["regions"] = aws_sdk_route53globalresolver.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("CreateGlobalResolverOutput.regions required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.cr_resource_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateGlobalResolverOutput.status required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("CreateGlobalResolverOutput.updated_at required")
    return out
