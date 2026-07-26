"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationStoreItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.annotation_store_item

AnnotationStoreItems: TypeAlias = list[
    "capo_omics.types.annotation_store_item.AnnotationStoreItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationStoreItems) -> list:
    import capo_omics.types.annotation_store_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.annotation_store_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnnotationStoreItems:
    import capo_omics.types.annotation_store_item

    out: AnnotationStoreItems = []
    for item in data:
        out.append(capo_omics.types.annotation_store_item.deserialize_json(item))
    return out
