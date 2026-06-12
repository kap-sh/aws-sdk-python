"""Generated from Smithy shape ``com.amazonaws.securityhub#Ipv6CidrBlockAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.ipv6_cidr_block_association

Ipv6CidrBlockAssociationList: TypeAlias = list[
    "aws_sdk_securityhub.types.ipv6_cidr_block_association.Ipv6CidrBlockAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: Ipv6CidrBlockAssociationList) -> list:
    import aws_sdk_securityhub.types.ipv6_cidr_block_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.ipv6_cidr_block_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Ipv6CidrBlockAssociationList:
    import aws_sdk_securityhub.types.ipv6_cidr_block_association

    out: Ipv6CidrBlockAssociationList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.ipv6_cidr_block_association.deserialize_json(item)
        )
    return out
