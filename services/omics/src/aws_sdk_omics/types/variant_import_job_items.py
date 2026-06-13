"""Generated from Smithy shape ``com.amazonaws.omics#VariantImportJobItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.variant_import_job_item

VariantImportJobItems: TypeAlias = list[
    "aws_sdk_omics.types.variant_import_job_item.VariantImportJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: VariantImportJobItems) -> list:
    import aws_sdk_omics.types.variant_import_job_item

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.variant_import_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> VariantImportJobItems:
    import aws_sdk_omics.types.variant_import_job_item

    out: VariantImportJobItems = []
    for item in data:
        out.append(aws_sdk_omics.types.variant_import_job_item.deserialize_json(item))
    return out
