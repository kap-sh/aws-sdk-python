"""Generated from Smithy shape ``com.amazonaws.glacier#PartList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glacier.types.part_list_element

PartList: TypeAlias = list["capo_glacier.types.part_list_element.PartListElement"]


# --- restJson1 ser/de ---
def serialize_json(value: PartList) -> list:
    import capo_glacier.types.part_list_element

    out: list = []
    for item in value:
        out.append(capo_glacier.types.part_list_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> PartList:
    import capo_glacier.types.part_list_element

    out: PartList = []
    for item in data:
        out.append(capo_glacier.types.part_list_element.deserialize_json(item))
    return out
