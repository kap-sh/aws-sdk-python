"""Generated from Smithy shape ``com.amazonaws.omics#ImportReferenceJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.import_reference_job_item

ImportReferenceJobList: TypeAlias = list[
    "capo_omics.types.import_reference_job_item.ImportReferenceJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportReferenceJobList) -> list:
    import capo_omics.types.import_reference_job_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.import_reference_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportReferenceJobList:
    import capo_omics.types.import_reference_job_item

    out: ImportReferenceJobList = []
    for item in data:
        out.append(capo_omics.types.import_reference_job_item.deserialize_json(item))
    return out
