"""Generated from Smithy shape ``com.amazonaws.qapps#LibraryItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.library_item_member

LibraryItemList: TypeAlias = list[
    "capo_qapps.types.library_item_member.LibraryItemMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: LibraryItemList) -> list:
    import capo_qapps.types.library_item_member

    out: list = []
    for item in value:
        out.append(capo_qapps.types.library_item_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> LibraryItemList:
    import capo_qapps.types.library_item_member

    out: LibraryItemList = []
    for item in data:
        out.append(capo_qapps.types.library_item_member.deserialize_json(item))
    return out
