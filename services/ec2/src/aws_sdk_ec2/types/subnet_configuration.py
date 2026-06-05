"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class SubnetConfiguration(TypedDict):
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    ipv4: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address to assign to the endpoint network interface in the subnet. You must provide an IPv4 address if the VPC endpoint supports IPv4.</p> <p>If you specify an IPv4 address when modifying a VPC endpoint, we replace the existing endpoint network interface with a new endpoint network interface with this IP address. This process temporarily disconnects the subnet and the VPC endpoint.</p>"""
    ipv6: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 address to assign to the endpoint network interface in the subnet. You must provide an IPv6 address if the VPC endpoint supports IPv6.</p> <p>If you specify an IPv6 address when modifying a VPC endpoint, we replace the existing endpoint network interface with a new endpoint network interface with this IP address. This process temporarily disconnects the subnet and the VPC endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "ipv4" in value:
        pairs.append((f"{prefix}.Ipv4", str(value["ipv4"])))
    if "ipv6" in value:
        pairs.append((f"{prefix}.Ipv6", str(value["ipv6"])))


def deserialize_ec2_query(el: Element) -> SubnetConfiguration:
    out: SubnetConfiguration = {}  # type: ignore[typeddict-item]
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_ipv4 = el.find("Ipv4")
    if child_ipv4 is not None:
        out["ipv4"] = str(child_ipv4.text or "")
    child_ipv6 = el.find("Ipv6")
    if child_ipv6 is not None:
        out["ipv6"] = str(child_ipv6.text or "")
    return out
