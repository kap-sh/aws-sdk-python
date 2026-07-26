"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetAccessSourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.cidr
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.dns_protocol
    import capo_route53globalresolver.types.ip_address_type
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name_short


class GetAccessSourceOutput(TypedDict, closed=True):
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the access source.</p>"""
    cidr: "capo_route53globalresolver.types.cidr.Cidr"
    """<p>The IP range for the rule's parameters in CIDR notation.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the rule was created.</p>"""
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID for the rule.</p>"""
    ip_address_type: "capo_route53globalresolver.types.ip_address_type.IpAddressType"
    """<p>The IP address type.</p>"""
    name: NotRequired[
        "capo_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>Name for the access source.</p>"""
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID for the DNS view that the rule is associated to.</p>"""
    protocol: "capo_route53globalresolver.types.dns_protocol.DnsProtocol"
    """<p>The protocol determines how data is transmitted to a Global Resolver instance.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>Information about the status of the rule.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the access source was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessSourceOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["cidr"] = value["cidr"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    out["id"] = value["id"]
    import capo_route53globalresolver.types.ip_address_type

    out["ipAddressType"] = (
        capo_route53globalresolver.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    out["dnsViewId"] = value["dns_view_id"]
    import capo_route53globalresolver.types.dns_protocol

    out["protocol"] = capo_route53globalresolver.types.dns_protocol.serialize_json(
        value["protocol"]
    )
    import capo_route53globalresolver.types.cr_resource_status

    out["status"] = capo_route53globalresolver.types.cr_resource_status.serialize_json(
        value["status"]
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAccessSourceOutput:
    out: GetAccessSourceOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetAccessSourceOutput.arn required")
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    else:
        raise DeserializationError("GetAccessSourceOutput.cidr required")
    if "createdAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetAccessSourceOutput.created_at required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetAccessSourceOutput.id required")
    if "ipAddressType" in data:
        import capo_route53globalresolver.types.ip_address_type

        out["ip_address_type"] = (
            capo_route53globalresolver.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    else:
        raise DeserializationError("GetAccessSourceOutput.ip_address_type required")
    if "name" in data:
        out["name"] = data["name"]
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("GetAccessSourceOutput.dns_view_id required")
    if "protocol" in data:
        import capo_route53globalresolver.types.dns_protocol

        out["protocol"] = (
            capo_route53globalresolver.types.dns_protocol.deserialize_json(
                data["protocol"]
            )
        )
    else:
        raise DeserializationError("GetAccessSourceOutput.protocol required")
    if "status" in data:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetAccessSourceOutput.status required")
    if "updatedAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetAccessSourceOutput.updated_at required")
    return out
