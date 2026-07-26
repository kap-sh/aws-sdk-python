"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetUploadPartList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.read_set_upload_part_list_item

ReadSetUploadPartList: TypeAlias = list[
    "capo_omics.types.read_set_upload_part_list_item.ReadSetUploadPartListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetUploadPartList) -> list:
    import capo_omics.types.read_set_upload_part_list_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.read_set_upload_part_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReadSetUploadPartList:
    import capo_omics.types.read_set_upload_part_list_item

    out: ReadSetUploadPartList = []
    for item in data:
        out.append(
            capo_omics.types.read_set_upload_part_list_item.deserialize_json(item)
        )
    return out
