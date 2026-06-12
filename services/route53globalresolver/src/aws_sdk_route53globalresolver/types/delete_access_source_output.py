"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteAccessSourceOutput``."""

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


class DeleteAccessSourceOutput(TypedDict):
    arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the deleted access source.</p>"""
    cidr: "aws_sdk_route53globalresolver.types.cidr.Cidr"
    """<p>The IP address or CIDR range of the deleted access source.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the access source was originally created.</p>"""
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the deleted access source.</p>"""
    ip_address_type: "aws_sdk_route53globalresolver.types.ip_address_type.IpAddressType"
    """<p>The IP address type of the deleted access source (IPv4 or IPv6).</p>"""
    name: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>The name of the deleted access source.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view that was associated with the deleted access source.</p>"""
    protocol: "aws_sdk_route53globalresolver.types.dns_protocol.DnsProtocol"
    """<p>The DNS protocol that was permitted for the deleted access source.</p>"""
    status: "aws_sdk_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The final status of the deleted access source.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the access source was last updated before deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessSourceOutput) -> dict:
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


def deserialize_json(data: dict) -> DeleteAccessSourceOutput:
    out: DeleteAccessSourceOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteAccessSourceOutput.arn required")
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    else:
        raise DeserializationError("DeleteAccessSourceOutput.cidr required")
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DeleteAccessSourceOutput.created_at required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteAccessSourceOutput.id required")
    if "ipAddressType" in data:
        import aws_sdk_route53globalresolver.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_route53globalresolver.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    else:
        raise DeserializationError("DeleteAccessSourceOutput.ip_address_type required")
    if "name" in data:
        out["name"] = data["name"]
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("DeleteAccessSourceOutput.dns_view_id required")
    if "protocol" in data:
        import aws_sdk_route53globalresolver.types.dns_protocol

        out["protocol"] = (
            aws_sdk_route53globalresolver.types.dns_protocol.deserialize_json(
                data["protocol"]
            )
        )
    else:
        raise DeserializationError("DeleteAccessSourceOutput.protocol required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.cr_resource_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteAccessSourceOutput.status required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DeleteAccessSourceOutput.updated_at required")
    return out
