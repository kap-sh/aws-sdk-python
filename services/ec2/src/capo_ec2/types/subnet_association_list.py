"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.subnet_association

SubnetAssociationList: TypeAlias = list[
    "capo_ec2.types.subnet_association.SubnetAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.subnet_association

        capo_ec2.types.subnet_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SubnetAssociationList:
    import capo_ec2.types.subnet_association

    out: SubnetAssociationList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.subnet_association.deserialize_ec2_query(child))
    return out
