"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupVpcAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_vpc_association

SecurityGroupVpcAssociationList: TypeAlias = list[
    "capo_ec2.types.security_group_vpc_association.SecurityGroupVpcAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupVpcAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.security_group_vpc_association

        capo_ec2.types.security_group_vpc_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SecurityGroupVpcAssociationList:
    import capo_ec2.types.security_group_vpc_association

    out: SecurityGroupVpcAssociationList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.security_group_vpc_association.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> SecurityGroupVpcAssociationList:
    import capo_ec2.types.security_group_vpc_association

    out: SecurityGroupVpcAssociationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.security_group_vpc_association.deserialize_ec2_query(child)
        )
    return out
