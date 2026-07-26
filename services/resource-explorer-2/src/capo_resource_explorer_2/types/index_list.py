"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#IndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.index

IndexList: TypeAlias = list["capo_resource_explorer_2.types.index.Index"]


# --- restJson1 ser/de ---
def serialize_json(value: IndexList) -> list:
    import capo_resource_explorer_2.types.index

    out: list = []
    for item in value:
        out.append(capo_resource_explorer_2.types.index.serialize_json(item))
    return out


def deserialize_json(data: list) -> IndexList:
    import capo_resource_explorer_2.types.index

    out: IndexList = []
    for item in data:
        out.append(capo_resource_explorer_2.types.index.deserialize_json(item))
    return out
