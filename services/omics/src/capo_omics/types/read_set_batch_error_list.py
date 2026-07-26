"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetBatchErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.read_set_batch_error

ReadSetBatchErrorList: TypeAlias = list[
    "capo_omics.types.read_set_batch_error.ReadSetBatchError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetBatchErrorList) -> list:
    import capo_omics.types.read_set_batch_error

    out: list = []
    for item in value:
        out.append(capo_omics.types.read_set_batch_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReadSetBatchErrorList:
    import capo_omics.types.read_set_batch_error

    out: ReadSetBatchErrorList = []
    for item in data:
        out.append(capo_omics.types.read_set_batch_error.deserialize_json(item))
    return out
