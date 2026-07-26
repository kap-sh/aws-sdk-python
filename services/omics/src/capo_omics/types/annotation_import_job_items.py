"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationImportJobItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.annotation_import_job_item

AnnotationImportJobItems: TypeAlias = list[
    "capo_omics.types.annotation_import_job_item.AnnotationImportJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationImportJobItems) -> list:
    import capo_omics.types.annotation_import_job_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.annotation_import_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnnotationImportJobItems:
    import capo_omics.types.annotation_import_job_item

    out: AnnotationImportJobItems = []
    for item in data:
        out.append(capo_omics.types.annotation_import_job_item.deserialize_json(item))
    return out
