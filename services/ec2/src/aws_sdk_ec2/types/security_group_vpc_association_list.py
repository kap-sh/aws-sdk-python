"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupVpcAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_vpc_association

SecurityGroupVpcAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_vpc_association.SecurityGroupVpcAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupVpcAssociationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.security_group_vpc_association

        aws_sdk_ec2.types.security_group_vpc_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SecurityGroupVpcAssociationList:
    import aws_sdk_ec2.types.security_group_vpc_association

    out: SecurityGroupVpcAssociationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.security_group_vpc_association.deserialize_ec2_query(
                child
            )
        )
    return out
