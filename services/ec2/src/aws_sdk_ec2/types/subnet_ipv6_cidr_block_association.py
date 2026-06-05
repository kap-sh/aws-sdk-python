"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetIpv6CidrBlockAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_source
    import aws_sdk_ec2.types.ipv6_address_attribute
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_cidr_association_id
    import aws_sdk_ec2.types.subnet_cidr_block_state


class SubnetIpv6CidrBlockAssociation(TypedDict):
    association_id: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_association_id.SubnetCidrAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR block.</p>"""
    ipv6_cidr_block_state: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_block_state.SubnetCidrBlockState"
    ]
    """<p>The state of the CIDR block.</p>"""
    ipv6_address_attribute: NotRequired[
        "aws_sdk_ec2.types.ipv6_address_attribute.Ipv6AddressAttribute"
    ]
    """<p>Public IPv6 addresses are those advertised on the internet from Amazon Web Services. Private IP addresses are not and cannot be advertised on the internet from Amazon Web Services.</p>"""
    ip_source: NotRequired["aws_sdk_ec2.types.ip_source.IpSource"]
    """<p>The source that allocated the IP address space. <code>byoip</code> or <code>amazon</code> indicates public IP address space allocated by Amazon or space that you have allocated with Bring your own IP (BYOIP). <code>none</code> indicates private space.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetIpv6CidrBlockAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "ipv6_cidr_block" in value:
        pairs.append((f"{prefix}.Ipv6CidrBlock", str(value["ipv6_cidr_block"])))
    if "ipv6_cidr_block_state" in value:
        import aws_sdk_ec2.types.subnet_cidr_block_state

        aws_sdk_ec2.types.subnet_cidr_block_state.serialize_ec2_query(
            value["ipv6_cidr_block_state"], pairs, f"{prefix}.Ipv6CidrBlockState"
        )
    if "ipv6_address_attribute" in value:
        import aws_sdk_ec2.types.ipv6_address_attribute

        aws_sdk_ec2.types.ipv6_address_attribute.serialize_ec2_query(
            value["ipv6_address_attribute"], pairs, f"{prefix}.Ipv6AddressAttribute"
        )
    if "ip_source" in value:
        import aws_sdk_ec2.types.ip_source

        aws_sdk_ec2.types.ip_source.serialize_ec2_query(
            value["ip_source"], pairs, f"{prefix}.IpSource"
        )


def deserialize_ec2_query(el: Element) -> SubnetIpv6CidrBlockAssociation:
    out: SubnetIpv6CidrBlockAssociation = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_ipv6_cidr_block = el.find("Ipv6CidrBlock")
    if child_ipv6_cidr_block is not None:
        out["ipv6_cidr_block"] = str(child_ipv6_cidr_block.text or "")
    child_ipv6_cidr_block_state = el.find("Ipv6CidrBlockState")
    if child_ipv6_cidr_block_state is not None:
        import aws_sdk_ec2.types.subnet_cidr_block_state

        out["ipv6_cidr_block_state"] = (
            aws_sdk_ec2.types.subnet_cidr_block_state.deserialize_ec2_query(
                child_ipv6_cidr_block_state
            )
        )
    child_ipv6_address_attribute = el.find("Ipv6AddressAttribute")
    if child_ipv6_address_attribute is not None:
        import aws_sdk_ec2.types.ipv6_address_attribute

        out["ipv6_address_attribute"] = (
            aws_sdk_ec2.types.ipv6_address_attribute.deserialize_ec2_query(
                child_ipv6_address_attribute
            )
        )
    child_ip_source = el.find("IpSource")
    if child_ip_source is not None:
        import aws_sdk_ec2.types.ip_source

        out["ip_source"] = aws_sdk_ec2.types.ip_source.deserialize_ec2_query(
            child_ip_source
        )
    return out
