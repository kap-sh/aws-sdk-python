"""Generated from Smithy shape ``com.amazonaws.omics#VariantStoreItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.variant_store_item

VariantStoreItems: TypeAlias = list[
    "aws_sdk_omics.types.variant_store_item.VariantStoreItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: VariantStoreItems) -> list:
    import aws_sdk_omics.types.variant_store_item

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.variant_store_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> VariantStoreItems:
    import aws_sdk_omics.types.variant_store_item

    out: VariantStoreItems = []
    for item in data:
        out.append(aws_sdk_omics.types.variant_store_item.deserialize_json(item))
    return out
