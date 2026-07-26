"""Generated from Smithy shape ``com.amazonaws.networkmanager#PrefixListAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.prefix_list_association

PrefixListAssociationList: TypeAlias = list[
    "capo_networkmanager.types.prefix_list_association.PrefixListAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrefixListAssociationList) -> list:
    import capo_networkmanager.types.prefix_list_association

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.prefix_list_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PrefixListAssociationList:
    import capo_networkmanager.types.prefix_list_association

    out: PrefixListAssociationList = []
    for item in data:
        out.append(
            capo_networkmanager.types.prefix_list_association.deserialize_json(item)
        )
    return out
