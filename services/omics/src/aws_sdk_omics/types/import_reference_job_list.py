"""Generated from Smithy shape ``com.amazonaws.omics#ImportReferenceJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.import_reference_job_item

ImportReferenceJobList: TypeAlias = list[
    "aws_sdk_omics.types.import_reference_job_item.ImportReferenceJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportReferenceJobList) -> list:
    import aws_sdk_omics.types.import_reference_job_item

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.import_reference_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportReferenceJobList:
    import aws_sdk_omics.types.import_reference_job_item

    out: ImportReferenceJobList = []
    for item in data:
        out.append(aws_sdk_omics.types.import_reference_job_item.deserialize_json(item))
    return out
