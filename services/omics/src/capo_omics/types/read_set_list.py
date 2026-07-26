"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.read_set_list_item

ReadSetList: TypeAlias = list["capo_omics.types.read_set_list_item.ReadSetListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetList) -> list:
    import capo_omics.types.read_set_list_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.read_set_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReadSetList:
    import capo_omics.types.read_set_list_item

    out: ReadSetList = []
    for item in data:
        out.append(capo_omics.types.read_set_list_item.deserialize_json(item))
    return out
