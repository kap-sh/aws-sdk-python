"""Generated from Smithy shape ``com.amazonaws.omics#StartReferenceImportJobSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.start_reference_import_job_source_item

StartReferenceImportJobSourceList: TypeAlias = list[
    "aws_sdk_omics.types.start_reference_import_job_source_item.StartReferenceImportJobSourceItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartReferenceImportJobSourceList) -> list:
    import aws_sdk_omics.types.start_reference_import_job_source_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_omics.types.start_reference_import_job_source_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StartReferenceImportJobSourceList:
    import aws_sdk_omics.types.start_reference_import_job_source_item

    out: StartReferenceImportJobSourceList = []
    for item in data:
        out.append(
            aws_sdk_omics.types.start_reference_import_job_source_item.deserialize_json(
                item
            )
        )
    return out
