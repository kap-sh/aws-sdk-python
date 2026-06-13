"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationStoreVersionItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.annotation_store_version_item

AnnotationStoreVersionItems: TypeAlias = list[
    "aws_sdk_omics.types.annotation_store_version_item.AnnotationStoreVersionItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationStoreVersionItems) -> list:
    import aws_sdk_omics.types.annotation_store_version_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_omics.types.annotation_store_version_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnnotationStoreVersionItems:
    import aws_sdk_omics.types.annotation_store_version_item

    out: AnnotationStoreVersionItems = []
    for item in data:
        out.append(
            aws_sdk_omics.types.annotation_store_version_item.deserialize_json(item)
        )
    return out
