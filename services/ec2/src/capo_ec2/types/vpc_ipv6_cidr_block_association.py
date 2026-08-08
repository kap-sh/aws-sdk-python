"""Generated from Smithy shape ``com.amazonaws.ec2#VpcIpv6CidrBlockAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ip_source
    import capo_ec2.types.ipv6_address_attribute
    import capo_ec2.types.string
    import capo_ec2.types.vpc_cidr_block_state


class VpcIpv6CidrBlockAssociation(TypedDict, closed=True):
    association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The association ID for the IPv6 CIDR block.</p>"""
    ipv6_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 CIDR block.</p>"""
    ipv6_cidr_block_state: NotRequired[
        "capo_ec2.types.vpc_cidr_block_state.VpcCidrBlockState"
    ]
    """<p>Information about the state of the CIDR block.</p>"""
    network_border_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses, for example, <code>us-east-1-wl1-bos-wlz-1</code>.</p>"""
    ipv6_pool: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the IPv6 address pool from which the IPv6 CIDR block is allocated.</p>"""
    ipv6_address_attribute: NotRequired[
        "capo_ec2.types.ipv6_address_attribute.Ipv6AddressAttribute"
    ]
    """<p>Public IPv6 addresses are those advertised on the internet from Amazon Web Services. Private IP addresses are not and cannot be advertised on the internet from Amazon Web Services.</p>"""
    ip_source: NotRequired["capo_ec2.types.ip_source.IpSource"]
    """<p>The source that allocated the IP address space. <code>byoip</code> or <code>amazon</code> indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). <code>none</code> indicates private space.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcIpv6CidrBlockAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association_id" in value:
        pairs.append((f"{key_prefix}AssociationId", str(value["association_id"])))
    if "ipv6_cidr_block" in value:
        pairs.append((f"{key_prefix}Ipv6CidrBlock", str(value["ipv6_cidr_block"])))
    if "ipv6_cidr_block_state" in value:
        import capo_ec2.types.vpc_cidr_block_state

        capo_ec2.types.vpc_cidr_block_state.serialize_ec2_query(
            value["ipv6_cidr_block_state"], pairs, f"{key_prefix}Ipv6CidrBlockState"
        )
    if "network_border_group" in value:
        pairs.append(
            (f"{key_prefix}NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "ipv6_pool" in value:
        pairs.append((f"{key_prefix}Ipv6Pool", str(value["ipv6_pool"])))
    if "ipv6_address_attribute" in value:
        import capo_ec2.types.ipv6_address_attribute

        capo_ec2.types.ipv6_address_attribute.serialize_ec2_query(
            value["ipv6_address_attribute"], pairs, f"{key_prefix}Ipv6AddressAttribute"
        )
    if "ip_source" in value:
        import capo_ec2.types.ip_source

        capo_ec2.types.ip_source.serialize_ec2_query(
            value["ip_source"], pairs, f"{key_prefix}IpSource"
        )


def deserialize_ec2_query(el: Element) -> VpcIpv6CidrBlockAssociation:
    out: VpcIpv6CidrBlockAssociation = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("associationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_ipv6_cidr_block = el.find("ipv6CidrBlock")
    if child_ipv6_cidr_block is not None:
        out["ipv6_cidr_block"] = str(child_ipv6_cidr_block.text or "")
    child_ipv6_cidr_block_state = el.find("ipv6CidrBlockState")
    if child_ipv6_cidr_block_state is not None:
        import capo_ec2.types.vpc_cidr_block_state

        out["ipv6_cidr_block_state"] = (
            capo_ec2.types.vpc_cidr_block_state.deserialize_ec2_query(
                child_ipv6_cidr_block_state
            )
        )
    child_network_border_group = el.find("networkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    child_ipv6_pool = el.find("ipv6Pool")
    if child_ipv6_pool is not None:
        out["ipv6_pool"] = str(child_ipv6_pool.text or "")
    child_ipv6_address_attribute = el.find("ipv6AddressAttribute")
    if child_ipv6_address_attribute is not None:
        import capo_ec2.types.ipv6_address_attribute

        out["ipv6_address_attribute"] = (
            capo_ec2.types.ipv6_address_attribute.deserialize_ec2_query(
                child_ipv6_address_attribute
            )
        )
    child_ip_source = el.find("ipSource")
    if child_ip_source is not None:
        import capo_ec2.types.ip_source

        out["ip_source"] = capo_ec2.types.ip_source.deserialize_ec2_query(
            child_ip_source
        )
    return out
