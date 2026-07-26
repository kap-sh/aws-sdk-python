"""Generated from Smithy shape ``com.amazonaws.omics#CompleteReadSetUploadPartList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.complete_read_set_upload_part_list_item

CompleteReadSetUploadPartList: TypeAlias = list[
    "capo_omics.types.complete_read_set_upload_part_list_item.CompleteReadSetUploadPartListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompleteReadSetUploadPartList) -> list:
    import capo_omics.types.complete_read_set_upload_part_list_item

    out: list = []
    for item in value:
        out.append(
            capo_omics.types.complete_read_set_upload_part_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CompleteReadSetUploadPartList:
    import capo_omics.types.complete_read_set_upload_part_list_item

    out: CompleteReadSetUploadPartList = []
    for item in data:
        out.append(
            capo_omics.types.complete_read_set_upload_part_list_item.deserialize_json(
                item
            )
        )
    return out
