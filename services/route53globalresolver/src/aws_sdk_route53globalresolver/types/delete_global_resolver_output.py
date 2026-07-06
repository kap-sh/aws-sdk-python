"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteGlobalResolverOutput``."""

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


class DeleteGlobalResolverOutput(TypedDict, closed=True):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted Route 53 Global Resolver.</p>"""
    arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the deleted Route 53 Global Resolver.</p>"""
    client_token: "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    dns_name: "aws_sdk_route53globalresolver.types.sni.Sni"
    """<p>The hostname that DNS clients used for TLS certificate validation when connecting to the deleted Route 53 Global Resolver.</p>"""
    observability_region: NotRequired[
        "aws_sdk_route53globalresolver.types.region.Region"
    ]
    """<p>The Amazon Web Services Region where observability data for the deleted Route 53 Global Resolver was stored.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the deleted Route 53 Global Resolver.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the deleted Route 53 Global Resolver.</p>"""
    regions: "aws_sdk_route53globalresolver.types.regions.Regions"
    """<p>The Amazon Web Services Regions where the deleted Route 53 Global Resolver was deployed and operational.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the Route 53 Global Resolver was originally created.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the Route 53 Global Resolver was last updated before deletion.</p>"""
    status: "aws_sdk_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The final status of the deleted Route 53 Global Resolver.</p>"""
    ipv4_addresses: "aws_sdk_route53globalresolver.types.i_pv4_addresses.IPv4Addresses"
    """<p>The global anycast IPv4 addresses that were associated with the deleted Route 53 Global Resolver.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_route53globalresolver.types.i_pv6_addresses.IPv6Addresses"
    ]
    """<p>The global anycast IPv6 addresses that were associated with the deleted Route 53 Global Resolver.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.GlobalResolverIpAddressType"
    ]
    """<p>The IP address type that was configured for the deleted Route 53 Global Resolver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGlobalResolverOutput) -> dict:
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
    import aws_sdk_route53globalresolver.types.regions

    out["regions"] = aws_sdk_route53globalresolver.types.regions.serialize_json(
        value["regions"]
    )
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
    import aws_sdk_route53globalresolver.types.cr_resource_status

    out["status"] = (
        aws_sdk_route53globalresolver.types.cr_resource_status.serialize_json(
            value["status"]
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
    if "ip_address_type" in value:
        import aws_sdk_route53globalresolver.types.global_resolver_ip_address_type

        out["ipAddressType"] = (
            aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteGlobalResolverOutput:
    out: DeleteGlobalResolverOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.client_token required")
    if "dnsName" in data:
        out["dns_name"] = data["dnsName"]
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.dns_name required")
    if "observabilityRegion" in data:
        out["observability_region"] = data["observabilityRegion"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "regions" in data:
        import aws_sdk_route53globalresolver.types.regions

        out["regions"] = aws_sdk_route53globalresolver.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.regions required")
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.updated_at required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.cr_resource_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.status required")
    if "ipv4Addresses" in data:
        import aws_sdk_route53globalresolver.types.i_pv4_addresses

        out["ipv4_addresses"] = (
            aws_sdk_route53globalresolver.types.i_pv4_addresses.deserialize_json(
                data["ipv4Addresses"]
            )
        )
    else:
        raise DeserializationError("DeleteGlobalResolverOutput.ipv4_addresses required")
    if "ipv6Addresses" in data:
        import aws_sdk_route53globalresolver.types.i_pv6_addresses

        out["ipv6_addresses"] = (
            aws_sdk_route53globalresolver.types.i_pv6_addresses.deserialize_json(
                data["ipv6Addresses"]
            )
        )
    if "ipAddressType" in data:
        import aws_sdk_route53globalresolver.types.global_resolver_ip_address_type

        out["ip_address_type"] = (
            aws_sdk_route53globalresolver.types.global_resolver_ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    return out
