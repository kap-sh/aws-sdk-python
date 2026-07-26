"""Generated from Smithy shape ``com.amazonaws.omics#VariantImportItemDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.variant_import_item_detail

VariantImportItemDetails: TypeAlias = list[
    "capo_omics.types.variant_import_item_detail.VariantImportItemDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: VariantImportItemDetails) -> list:
    import capo_omics.types.variant_import_item_detail

    out: list = []
    for item in value:
        out.append(capo_omics.types.variant_import_item_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> VariantImportItemDetails:
    import capo_omics.types.variant_import_item_detail

    out: VariantImportItemDetails = []
    for item in data:
        out.append(capo_omics.types.variant_import_item_detail.deserialize_json(item))
    return out
