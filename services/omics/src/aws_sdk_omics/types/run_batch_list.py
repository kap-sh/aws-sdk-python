"""Generated from Smithy shape ``com.amazonaws.omics#RunBatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_batch_list_item

RunBatchList: TypeAlias = list[
    "aws_sdk_omics.types.run_batch_list_item.RunBatchListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: RunBatchList) -> list:
    import aws_sdk_omics.types.run_batch_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.run_batch_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RunBatchList:
    import aws_sdk_omics.types.run_batch_list_item

    out: RunBatchList = []
    for item in data:
        out.append(aws_sdk_omics.types.run_batch_list_item.deserialize_json(item))
    return out
