"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateAccessSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.cidr
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.dns_protocol
    import aws_sdk_route53globalresolver.types.ip_address_type
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name_short
    import aws_sdk_route53globalresolver.types.tags


class CreateAccessSourceInput(TypedDict, closed=True):
    cidr: "aws_sdk_route53globalresolver.types.cidr.Cidr"
    """<p>The IP address or CIDR range that is allowed to send DNS queries to the Route 53 Global Resolver.</p>"""
    client_token: NotRequired[
        "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique string that identifies the request and ensures idempotency.</p>"""
    ip_address_type: "aws_sdk_route53globalresolver.types.ip_address_type.IpAddressType"
    """<p>The IP address type for this access source. Valid values are IPv4 and IPv6 (if the Route 53 Global Resolver supports dual-stack).</p>"""
    name: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
    ]
    """<p>A descriptive name for the access source.</p>"""
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view to associate with this access source.</p>"""
    protocol: "aws_sdk_route53globalresolver.types.dns_protocol.DnsProtocol"
    """<p>The DNS protocol that is permitted for this access source. Valid values are Do53 (DNS over port 53), DoT (DNS over TLS), and DoH (DNS over HTTPS).</p>"""
    tags: NotRequired["aws_sdk_route53globalresolver.types.tags.Tags"]
    """<p>Tags to associate with the access source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessSourceInput) -> dict:
    out: dict = {}
    out["cidr"] = value["cidr"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_route53globalresolver.types.ip_address_type

    out["ipAddressType"] = (
        aws_sdk_route53globalresolver.types.ip_address_type.serialize_json(
            value.get("ip_address_type", "IPV4")
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    out["dnsViewId"] = value["dns_view_id"]
    import aws_sdk_route53globalresolver.types.dns_protocol

    out["protocol"] = aws_sdk_route53globalresolver.types.dns_protocol.serialize_json(
        value["protocol"]
    )
    if "tags" in value:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateAccessSourceInput:
    out: CreateAccessSourceInput = {}  # type: ignore[typeddict-item]
    if "cidr" in data:
        out["cidr"] = data["cidr"]
    else:
        raise DeserializationError("CreateAccessSourceInput.cidr required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "ipAddressType" in data:
        import aws_sdk_route53globalresolver.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_route53globalresolver.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    else:
        out["ip_address_type"] = "IPV4"
    if "name" in data:
        out["name"] = data["name"]
    if "dnsViewId" in data:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        raise DeserializationError("CreateAccessSourceInput.dns_view_id required")
    if "protocol" in data:
        import aws_sdk_route53globalresolver.types.dns_protocol

        out["protocol"] = (
            aws_sdk_route53globalresolver.types.dns_protocol.deserialize_json(
                data["protocol"]
            )
        )
    else:
        raise DeserializationError("CreateAccessSourceInput.protocol required")
    if "tags" in data:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.deserialize_json(
            data["tags"]
        )
    return out
