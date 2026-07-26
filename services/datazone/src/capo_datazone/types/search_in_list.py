"""Generated from Smithy shape ``com.amazonaws.datazone#SearchInList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.search_in_item

SearchInList: TypeAlias = list["capo_datazone.types.search_in_item.SearchInItem"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchInList) -> list:
    import capo_datazone.types.search_in_item

    out: list = []
    for item in value:
        out.append(capo_datazone.types.search_in_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchInList:
    import capo_datazone.types.search_in_item

    out: SearchInList = []
    for item in data:
        out.append(capo_datazone.types.search_in_item.deserialize_json(item))
    return out
