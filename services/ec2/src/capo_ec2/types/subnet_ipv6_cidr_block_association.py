"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetIpv6CidrBlockAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ip_source
    import capo_ec2.types.ipv6_address_attribute
    import capo_ec2.types.string
    import capo_ec2.types.subnet_cidr_association_id
    import capo_ec2.types.subnet_cidr_block_state


class SubnetIpv6CidrBlockAssociation(TypedDict, closed=True):
    association_id: NotRequired[
        "capo_ec2.types.subnet_cidr_association_id.SubnetCidrAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    ipv6_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 CIDR block.</p>"""
    ipv6_cidr_block_state: NotRequired[
        "capo_ec2.types.subnet_cidr_block_state.SubnetCidrBlockState"
    ]
    """<p>The state of the CIDR block.</p>"""
    ipv6_address_attribute: NotRequired[
        "capo_ec2.types.ipv6_address_attribute.Ipv6AddressAttribute"
    ]
    """<p>Public IPv6 addresses are those advertised on the internet from Amazon Web Services. Private IP addresses are not and cannot be advertised on the internet from Amazon Web Services.</p>"""
    ip_source: NotRequired["capo_ec2.types.ip_source.IpSource"]
    """<p>The source that allocated the IP address space. <code>byoip</code> or <code>amazon</code> indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). <code>none</code> indicates private space.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetIpv6CidrBlockAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association_id" in value:
        pairs.append((f"{key_prefix}AssociationId", str(value["association_id"])))
    if "ipv6_cidr_block" in value:
        pairs.append((f"{key_prefix}Ipv6CidrBlock", str(value["ipv6_cidr_block"])))
    if "ipv6_cidr_block_state" in value:
        import capo_ec2.types.subnet_cidr_block_state

        capo_ec2.types.subnet_cidr_block_state.serialize_ec2_query(
            value["ipv6_cidr_block_state"], pairs, f"{key_prefix}Ipv6CidrBlockState"
        )
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


def deserialize_ec2_query(el: Element) -> SubnetIpv6CidrBlockAssociation:
    out: SubnetIpv6CidrBlockAssociation = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("associationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_ipv6_cidr_block = el.find("ipv6CidrBlock")
    if child_ipv6_cidr_block is not None:
        out["ipv6_cidr_block"] = str(child_ipv6_cidr_block.text or "")
    child_ipv6_cidr_block_state = el.find("ipv6CidrBlockState")
    if child_ipv6_cidr_block_state is not None:
        import capo_ec2.types.subnet_cidr_block_state

        out["ipv6_cidr_block_state"] = (
            capo_ec2.types.subnet_cidr_block_state.deserialize_ec2_query(
                child_ipv6_cidr_block_state
            )
        )
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
