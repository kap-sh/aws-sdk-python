"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateIpAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.ipv6
    import aws_sdk_route53resolver.types.resource_id


class UpdateIpAddress(TypedDict, closed=True):
    ip_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p> The ID of the IP address, specified by the <code>ResolverEndpointId</code>. </p>"""
    ipv6: "aws_sdk_route53resolver.types.ipv6.Ipv6"
    """<p> The IPv6 address that you want to use for DNS queries. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateIpAddress) -> dict:
    out: dict = {}
    out["IpId"] = value["ip_id"]
    out["Ipv6"] = value["ipv6"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateIpAddress:
    out: UpdateIpAddress = {}  # type: ignore[typeddict-item]
    if "IpId" in data:
        out["ip_id"] = data["IpId"]
    else:
        raise DeserializationError("UpdateIpAddress.ip_id required")
    if "Ipv6" in data:
        out["ipv6"] = data["Ipv6"]
    else:
        raise DeserializationError("UpdateIpAddress.ipv6 required")
    return out
