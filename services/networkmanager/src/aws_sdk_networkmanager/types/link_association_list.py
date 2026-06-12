"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.link_association

LinkAssociationList: TypeAlias = list[
    "aws_sdk_networkmanager.types.link_association.LinkAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkAssociationList) -> list:
    import aws_sdk_networkmanager.types.link_association

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.link_association.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinkAssociationList:
    import aws_sdk_networkmanager.types.link_association

    out: LinkAssociationList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.link_association.deserialize_json(item))
    return out
