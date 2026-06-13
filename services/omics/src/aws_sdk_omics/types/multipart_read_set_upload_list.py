"""Generated from Smithy shape ``com.amazonaws.omics#MultipartReadSetUploadList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.multipart_read_set_upload_list_item

MultipartReadSetUploadList: TypeAlias = list[
    "aws_sdk_omics.types.multipart_read_set_upload_list_item.MultipartReadSetUploadListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: MultipartReadSetUploadList) -> list:
    import aws_sdk_omics.types.multipart_read_set_upload_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_omics.types.multipart_read_set_upload_list_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MultipartReadSetUploadList:
    import aws_sdk_omics.types.multipart_read_set_upload_list_item

    out: MultipartReadSetUploadList = []
    for item in data:
        out.append(
            aws_sdk_omics.types.multipart_read_set_upload_list_item.deserialize_json(
                item
            )
        )
    return out
