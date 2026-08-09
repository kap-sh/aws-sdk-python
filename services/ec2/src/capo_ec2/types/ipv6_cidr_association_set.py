"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6CidrAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv6_cidr_association

Ipv6CidrAssociationSet: TypeAlias = list[
    "capo_ec2.types.ipv6_cidr_association.Ipv6CidrAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6CidrAssociationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipv6_cidr_association

        capo_ec2.types.ipv6_cidr_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> Ipv6CidrAssociationSet:
    import capo_ec2.types.ipv6_cidr_association

    out: Ipv6CidrAssociationSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ipv6_cidr_association.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> Ipv6CidrAssociationSet:
    import capo_ec2.types.ipv6_cidr_association

    out: Ipv6CidrAssociationSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipv6_cidr_association.deserialize_ec2_query(child))
    return out
