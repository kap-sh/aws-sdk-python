"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateAccessSourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.cidr
    import aws_sdk_route53globalresolver.types.dns_protocol
    import aws_sdk_route53globalresolver.types.ip_address_type
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name_short


class UpdateAccessSourceInput(TypedDict):
    access_source_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the access source to update.</p>"""
    cidr: NotRequired["aws_sdk_route53globalresolver.types.cidr.Cidr"]
    """<p>The CIDR block for the access source.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_route53globalresolver.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type for the access source.</p>"""
    name: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>The name of the access source.</p>"""
    protocol: NotRequired[
        "aws_sdk_route53globalresolver.types.dns_protocol.DnsProtocol"
    ]
    """<p>The protocol for the access source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessSourceInput) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    if "ip_address_type" in value:
        import aws_sdk_route53globalresolver.types.ip_address_type

        out["ipAddressType"] = (
            aws_sdk_route53globalresolver.types.ip_address_type.serialize_json(
                value["ip_address_type"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "protocol" in value:
        import aws_sdk_route53globalresolver.types.dns_protocol

        out["protocol"] = (
            aws_sdk_route53globalresolver.types.dns_protocol.serialize_json(
                value["protocol"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccessSourceInput:
    out: UpdateAccessSourceInput = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    if "ipAddressType" in data:
        import aws_sdk_route53globalresolver.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_route53globalresolver.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "protocol" in data:
        import aws_sdk_route53globalresolver.types.dns_protocol

        out["protocol"] = (
            aws_sdk_route53globalresolver.types.dns_protocol.deserialize_json(
                data["protocol"]
            )
        )
    return out
