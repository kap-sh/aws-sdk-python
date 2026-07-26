"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.reference_list_item

ReferenceList: TypeAlias = list[
    "capo_omics.types.reference_list_item.ReferenceListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceList) -> list:
    import capo_omics.types.reference_list_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.reference_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReferenceList:
    import capo_omics.types.reference_list_item

    out: ReferenceList = []
    for item in data:
        out.append(capo_omics.types.reference_list_item.deserialize_json(item))
    return out
