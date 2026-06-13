"""Generated from Smithy shape ``com.amazonaws.mgn#ImportFileEnrichmentsIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.import_file_enrichment_job_id

ImportFileEnrichmentsIDsFilter: TypeAlias = list[
    "aws_sdk_mgn.types.import_file_enrichment_job_id.ImportFileEnrichmentJobID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportFileEnrichmentsIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> ImportFileEnrichmentsIDsFilter:
    return list(data)
