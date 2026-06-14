"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceIpv6Address``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class NetworkInterfaceIpv6Address(TypedDict):
    ipv6_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 address.</p>"""
    public_ipv6_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html\">EC2 instance hostnames, DNS names, and domains</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    is_primary_ipv6: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    r"""<p>Determines if an IPv6 address associated with a network interface is the primary IPv6 address. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyNetworkInterfaceAttribute.html\">ModifyNetworkInterfaceAttribute</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInterfaceIpv6Address, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_address" in value:
        pairs.append((f"{prefix}.Ipv6Address", str(value["ipv6_address"])))
    if "public_ipv6_dns_name" in value:
        pairs.append(
            (f"{prefix}.PublicIpv6DnsName", str(value["public_ipv6_dns_name"]))
        )
    if "is_primary_ipv6" in value:
        pairs.append(
            (f"{prefix}.IsPrimaryIpv6", "true" if value["is_primary_ipv6"] else "false")
        )


def deserialize_ec2_query(el: Element) -> NetworkInterfaceIpv6Address:
    out: NetworkInterfaceIpv6Address = {}  # type: ignore[typeddict-item]
    child_ipv6_address = el.find("Ipv6Address")
    if child_ipv6_address is not None:
        out["ipv6_address"] = str(child_ipv6_address.text or "")
    child_public_ipv6_dns_name = el.find("PublicIpv6DnsName")
    if child_public_ipv6_dns_name is not None:
        out["public_ipv6_dns_name"] = str(child_public_ipv6_dns_name.text or "")
    child_is_primary_ipv6 = el.find("IsPrimaryIpv6")
    if child_is_primary_ipv6 is not None:
        out["is_primary_ipv6"] = (child_is_primary_ipv6.text or "").lower() == "true"
    return out
