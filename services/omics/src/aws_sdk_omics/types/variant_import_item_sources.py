"""Generated from Smithy shape ``com.amazonaws.omics#VariantImportItemSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.variant_import_item_source

VariantImportItemSources: TypeAlias = list[
    "aws_sdk_omics.types.variant_import_item_source.VariantImportItemSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: VariantImportItemSources) -> list:
    import aws_sdk_omics.types.variant_import_item_source

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.variant_import_item_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> VariantImportItemSources:
    import aws_sdk_omics.types.variant_import_item_source

    out: VariantImportItemSources = []
    for item in data:
        out.append(
            aws_sdk_omics.types.variant_import_item_source.deserialize_json(item)
        )
    return out
