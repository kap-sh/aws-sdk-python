"""Generated from Smithy shape ``com.amazonaws.omics#RunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.run_list_item

RunList: TypeAlias = list["capo_omics.types.run_list_item.RunListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: RunList) -> list:
    import capo_omics.types.run_list_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.run_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RunList:
    import capo_omics.types.run_list_item

    out: RunList = []
    for item in data:
        out.append(capo_omics.types.run_list_item.deserialize_json(item))
    return out
