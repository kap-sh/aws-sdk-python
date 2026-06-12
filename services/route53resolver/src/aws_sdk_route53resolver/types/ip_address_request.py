"""Generated from Smithy shape ``com.amazonaws.route53resolver#IpAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.ip
    import aws_sdk_route53resolver.types.ipv6
    import aws_sdk_route53resolver.types.subnet_id


class IpAddressRequest(TypedDict):
    subnet_id: "aws_sdk_route53resolver.types.subnet_id.SubnetId"
    """<p>The ID of the subnet that contains the IP address. </p>"""
    ip: NotRequired["aws_sdk_route53resolver.types.ip.Ip"]
    """<p>The IPv4 address that you want to use for DNS queries.</p>"""
    ipv6: NotRequired["aws_sdk_route53resolver.types.ipv6.Ipv6"]
    """<p> The IPv6 address that you want to use for DNS queries. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressRequest) -> dict:
    out: dict = {}
    out["SubnetId"] = value["subnet_id"]
    if "ip" in value:
        out["Ip"] = value["ip"]
    if "ipv6" in value:
        out["Ipv6"] = value["ipv6"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpAddressRequest:
    out: IpAddressRequest = {}  # type: ignore[typeddict-item]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    else:
        raise DeserializationError("IpAddressRequest.subnet_id required")
    if "Ip" in data:
        out["ip"] = data["Ip"]
    if "Ipv6" in data:
        out["ipv6"] = data["Ipv6"]
    return out
