"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceStoreDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.reference_store_detail

ReferenceStoreDetailList: TypeAlias = list[
    "capo_omics.types.reference_store_detail.ReferenceStoreDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceStoreDetailList) -> list:
    import capo_omics.types.reference_store_detail

    out: list = []
    for item in value:
        out.append(capo_omics.types.reference_store_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReferenceStoreDetailList:
    import capo_omics.types.reference_store_detail

    out: ReferenceStoreDetailList = []
    for item in data:
        out.append(capo_omics.types.reference_store_detail.deserialize_json(item))
    return out
