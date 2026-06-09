"""Generated from Smithy shape ``com.amazonaws.ec2#AsnAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.asn_association

AsnAssociationSet: TypeAlias = list["aws_sdk_ec2.types.asn_association.AsnAssociation"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AsnAssociationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.asn_association

        aws_sdk_ec2.types.asn_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AsnAssociationSet:
    import aws_sdk_ec2.types.asn_association

    out: AsnAssociationSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.asn_association.deserialize_ec2_query(child))
    return out
