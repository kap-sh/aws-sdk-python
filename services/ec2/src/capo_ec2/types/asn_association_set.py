"""Generated from Smithy shape ``com.amazonaws.ec2#AsnAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.asn_association

AsnAssociationSet: TypeAlias = list["capo_ec2.types.asn_association.AsnAssociation"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AsnAssociationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.asn_association

        capo_ec2.types.asn_association.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> AsnAssociationSet:
    import capo_ec2.types.asn_association

    out: AsnAssociationSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.asn_association.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AsnAssociationSet:
    import capo_ec2.types.asn_association

    out: AsnAssociationSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.asn_association.deserialize_ec2_query(child))
    return out
