"""Generated from Smithy shape ``com.amazonaws.securityhub#CidrBlockAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.cidr_block_association

CidrBlockAssociationList: TypeAlias = list[
    "capo_securityhub.types.cidr_block_association.CidrBlockAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CidrBlockAssociationList) -> list:
    import capo_securityhub.types.cidr_block_association

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.cidr_block_association.serialize_json(item))
    return out


def deserialize_json(data: list) -> CidrBlockAssociationList:
    import capo_securityhub.types.cidr_block_association

    out: CidrBlockAssociationList = []
    for item in data:
        out.append(capo_securityhub.types.cidr_block_association.deserialize_json(item))
    return out
