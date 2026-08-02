"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateSubnetCidrBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.netmask_length
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id


class AssociateSubnetCidrBlockRequest(TypedDict, closed=True):
    ipv6_ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>An IPv6 IPAM pool ID.</p>"""
    ipv6_netmask_length: NotRequired["capo_ec2.types.netmask_length.NetmaskLength"]
    """<p>An IPv6 netmask length.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of your subnet.</p>"""
    ipv6_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 CIDR block for your subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateSubnetCidrBlockRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv6_ipam_pool_id" in value:
        pairs.append((f"{key_prefix}Ipv6IpamPoolId", str(value["ipv6_ipam_pool_id"])))
    if "ipv6_netmask_length" in value:
        pairs.append(
            (f"{key_prefix}Ipv6NetmaskLength", str(value["ipv6_netmask_length"]))
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "ipv6_cidr_block" in value:
        pairs.append((f"{key_prefix}Ipv6CidrBlock", str(value["ipv6_cidr_block"])))


def deserialize_ec2_query(el: Element) -> AssociateSubnetCidrBlockRequest:
    out: AssociateSubnetCidrBlockRequest = {}  # type: ignore[typeddict-item]
    child_ipv6_ipam_pool_id = el.find("Ipv6IpamPoolId")
    if child_ipv6_ipam_pool_id is not None:
        out["ipv6_ipam_pool_id"] = str(child_ipv6_ipam_pool_id.text or "")
    child_ipv6_netmask_length = el.find("Ipv6NetmaskLength")
    if child_ipv6_netmask_length is not None:
        out["ipv6_netmask_length"] = int(child_ipv6_netmask_length.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_ipv6_cidr_block = el.find("Ipv6CidrBlock")
    if child_ipv6_cidr_block is not None:
        out["ipv6_cidr_block"] = str(child_ipv6_cidr_block.text or "")
    return out
