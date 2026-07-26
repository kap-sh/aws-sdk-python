"""Generated from Smithy shape ``com.amazonaws.omics#StartReferenceImportJobSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.start_reference_import_job_source_item

StartReferenceImportJobSourceList: TypeAlias = list[
    "capo_omics.types.start_reference_import_job_source_item.StartReferenceImportJobSourceItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartReferenceImportJobSourceList) -> list:
    import capo_omics.types.start_reference_import_job_source_item

    out: list = []
    for item in value:
        out.append(
            capo_omics.types.start_reference_import_job_source_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StartReferenceImportJobSourceList:
    import capo_omics.types.start_reference_import_job_source_item

    out: StartReferenceImportJobSourceList = []
    for item in data:
        out.append(
            capo_omics.types.start_reference_import_job_source_item.deserialize_json(
                item
            )
        )
    return out
