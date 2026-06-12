"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#AccessSourcesItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.cidr
    import aws_sdk_route53globalresolver.types.cr_resource_status
    import aws_sdk_route53globalresolver.types.dns_protocol
    import aws_sdk_route53globalresolver.types.ip_address_type
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name_short


class AccessSourcesItem(TypedDict):
    arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the access source.</p>"""
    cidr: "aws_sdk_route53globalresolver.types.cidr.Cidr"
    """<p>The CIDR block that defines the IP address range for the access source.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the access source was created.</p>"""
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the access source.</p>"""
    ip_address_type: "aws_sdk_route53globalresolver.types.ip_address_type.IpAddressType"
    """<p>The IP address type of the access source.</p>"""
    name: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>The name of the access source.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view that the access source is associated with.</p>"""
    protocol: "aws_sdk_route53globalresolver.types.dns_protocol.DnsProtocol"
    """<p>The protocol used by the access source.</p>"""
    status: "aws_sdk_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The current status of the access source.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the access source was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessSourcesItem) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["cidr"] = value["cidr"]
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    out["id"] = value["id"]
    import aws_sdk_route53globalresolver.types.ip_address_type

    out["ipAddressType"] = (
        aws_sdk_route53globalresolver.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    out["dnsViewId"] = value["dns_view_id"]
    import aws_sdk_route53globalresolver.types.dns_protocol

    out["protocol"] = aws_sdk_route53globalresolver.types.dns_protocol.serialize_json(
        value["protocol"]
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


def deserialize_json(data: dict) -> AccessSourcesItem:
    out: AccessSourcesItem = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AccessSourcesItem.arn required")
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    else:
        raise DeserializationError("AccessSourcesItem.cidr required")
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("AccessSourcesItem.created_at required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AccessSourcesItem.id required")
    if "ipAddressType" in data:
        import aws_sdk_route53globalresolver.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_route53globalresolver.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    else:
        raise DeserializationError("AccessSourcesItem.ip_address_type required")
    if "name" in data:
        out["name"] = data["name"]
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("AccessSourcesItem.dns_view_id required")
    if "protocol" in data:
        import aws_sdk_route53globalresolver.types.dns_protocol

        out["protocol"] = (
            aws_sdk_route53globalresolver.types.dns_protocol.deserialize_json(
                data["protocol"]
            )
        )
    else:
        raise DeserializationError("AccessSourcesItem.protocol required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.cr_resource_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AccessSourcesItem.status required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("AccessSourcesItem.updated_at required")
    return out
