"""Generated from Smithy shape ``com.amazonaws.route53resolver#IpAddressUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.ip
    import capo_route53resolver.types.ipv6
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.subnet_id


class IpAddressUpdate(TypedDict, closed=True):
    ip_id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    r"""<p> <i>Only when removing an IP address from a Resolver endpoint</i>: The ID of the IP address that you want to remove. To get this ID, use <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html\">GetResolverEndpoint</a>.</p>"""
    subnet_id: NotRequired["capo_route53resolver.types.subnet_id.SubnetId"]
    r"""<p>The ID of the subnet that includes the IP address that you want to update. To get this ID, use <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html\">GetResolverEndpoint</a>.</p>"""
    ip: NotRequired["capo_route53resolver.types.ip.Ip"]
    """<p>The new IPv4 address.</p>"""
    ipv6: NotRequired["capo_route53resolver.types.ipv6.Ipv6"]
    """<p> The new IPv6 address. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressUpdate) -> dict:
    out: dict = {}
    if "ip_id" in value:
        out["IpId"] = value["ip_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "ip" in value:
        out["Ip"] = value["ip"]
    if "ipv6" in value:
        out["Ipv6"] = value["ipv6"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpAddressUpdate:
    out: IpAddressUpdate = {}  # type: ignore[typeddict-item]
    if "IpId" in data:
        out["ip_id"] = data["IpId"]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "Ip" in data:
        out["ip"] = data["Ip"]
    if "Ipv6" in data:
        out["ipv6"] = data["Ipv6"]
    return out
