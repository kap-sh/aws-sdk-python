"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationStoreItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.annotation_store_item

AnnotationStoreItems: TypeAlias = list[
    "aws_sdk_omics.types.annotation_store_item.AnnotationStoreItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationStoreItems) -> list:
    import aws_sdk_omics.types.annotation_store_item

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.annotation_store_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnnotationStoreItems:
    import aws_sdk_omics.types.annotation_store_item

    out: AnnotationStoreItems = []
    for item in data:
        out.append(aws_sdk_omics.types.annotation_store_item.deserialize_json(item))
    return out
