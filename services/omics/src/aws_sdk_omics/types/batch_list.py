"""Generated from Smithy shape ``com.amazonaws.omics#BatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_list_item

BatchList: TypeAlias = list["aws_sdk_omics.types.batch_list_item.BatchListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchList) -> list:
    import aws_sdk_omics.types.batch_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.batch_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchList:
    import aws_sdk_omics.types.batch_list_item

    out: BatchList = []
    for item in data:
        out.append(aws_sdk_omics.types.batch_list_item.deserialize_json(item))
    return out
