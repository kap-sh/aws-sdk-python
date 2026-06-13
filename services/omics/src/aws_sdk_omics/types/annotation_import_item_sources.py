"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationImportItemSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.annotation_import_item_source

AnnotationImportItemSources: TypeAlias = list[
    "aws_sdk_omics.types.annotation_import_item_source.AnnotationImportItemSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationImportItemSources) -> list:
    import aws_sdk_omics.types.annotation_import_item_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_omics.types.annotation_import_item_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnnotationImportItemSources:
    import aws_sdk_omics.types.annotation_import_item_source

    out: AnnotationImportItemSources = []
    for item in data:
        out.append(
            aws_sdk_omics.types.annotation_import_item_source.deserialize_json(item)
        )
    return out
