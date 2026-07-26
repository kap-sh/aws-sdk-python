"""Generated from Smithy shape ``com.amazonaws.resiliencehub#SortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.sort

SortList: TypeAlias = list["capo_resiliencehub.types.sort.Sort"]


# --- restJson1 ser/de ---
def serialize_json(value: SortList) -> list:
    import capo_resiliencehub.types.sort

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.sort.serialize_json(item))
    return out


def deserialize_json(data: list) -> SortList:
    import capo_resiliencehub.types.sort

    out: SortList = []
    for item in data:
        out.append(capo_resiliencehub.types.sort.deserialize_json(item))
    return out
