"""Generated from Smithy shape ``com.amazonaws.omics#RunBatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.run_batch_list_item

RunBatchList: TypeAlias = list["capo_omics.types.run_batch_list_item.RunBatchListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: RunBatchList) -> list:
    import capo_omics.types.run_batch_list_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.run_batch_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RunBatchList:
    import capo_omics.types.run_batch_list_item

    out: RunBatchList = []
    for item in data:
        out.append(capo_omics.types.run_batch_list_item.deserialize_json(item))
    return out
