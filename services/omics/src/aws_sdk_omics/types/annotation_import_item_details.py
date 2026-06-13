"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationImportItemDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.annotation_import_item_detail

AnnotationImportItemDetails: TypeAlias = list[
    "aws_sdk_omics.types.annotation_import_item_detail.AnnotationImportItemDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationImportItemDetails) -> list:
    import aws_sdk_omics.types.annotation_import_item_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_omics.types.annotation_import_item_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnnotationImportItemDetails:
    import aws_sdk_omics.types.annotation_import_item_detail

    out: AnnotationImportItemDetails = []
    for item in data:
        out.append(
            aws_sdk_omics.types.annotation_import_item_detail.deserialize_json(item)
        )
    return out
