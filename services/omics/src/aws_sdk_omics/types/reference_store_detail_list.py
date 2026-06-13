"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceStoreDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.reference_store_detail

ReferenceStoreDetailList: TypeAlias = list[
    "aws_sdk_omics.types.reference_store_detail.ReferenceStoreDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceStoreDetailList) -> list:
    import aws_sdk_omics.types.reference_store_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.reference_store_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReferenceStoreDetailList:
    import aws_sdk_omics.types.reference_store_detail

    out: ReferenceStoreDetailList = []
    for item in data:
        out.append(aws_sdk_omics.types.reference_store_detail.deserialize_json(item))
    return out
