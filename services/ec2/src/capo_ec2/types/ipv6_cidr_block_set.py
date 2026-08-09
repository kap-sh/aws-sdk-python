"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6CidrBlockSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv6_cidr_block

Ipv6CidrBlockSet: TypeAlias = list["capo_ec2.types.ipv6_cidr_block.Ipv6CidrBlock"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6CidrBlockSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipv6_cidr_block

        capo_ec2.types.ipv6_cidr_block.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> Ipv6CidrBlockSet:
    import capo_ec2.types.ipv6_cidr_block

    out: Ipv6CidrBlockSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ipv6_cidr_block.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> Ipv6CidrBlockSet:
    import capo_ec2.types.ipv6_cidr_block

    out: Ipv6CidrBlockSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipv6_cidr_block.deserialize_ec2_query(child))
    return out
