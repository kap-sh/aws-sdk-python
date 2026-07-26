"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.resource_share_association

ResourceShareAssociationList: TypeAlias = list[
    "capo_ram.types.resource_share_association.ResourceShareAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareAssociationList) -> list:
    import capo_ram.types.resource_share_association

    out: list = []
    for item in value:
        out.append(capo_ram.types.resource_share_association.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceShareAssociationList:
    import capo_ram.types.resource_share_association

    out: ResourceShareAssociationList = []
    for item in data:
        out.append(capo_ram.types.resource_share_association.deserialize_json(item))
    return out
