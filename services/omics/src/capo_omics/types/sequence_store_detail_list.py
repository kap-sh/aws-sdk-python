"""Generated from Smithy shape ``com.amazonaws.omics#SequenceStoreDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.sequence_store_detail

SequenceStoreDetailList: TypeAlias = list[
    "capo_omics.types.sequence_store_detail.SequenceStoreDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SequenceStoreDetailList) -> list:
    import capo_omics.types.sequence_store_detail

    out: list = []
    for item in value:
        out.append(capo_omics.types.sequence_store_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> SequenceStoreDetailList:
    import capo_omics.types.sequence_store_detail

    out: SequenceStoreDetailList = []
    for item in data:
        out.append(capo_omics.types.sequence_store_detail.deserialize_json(item))
    return out
