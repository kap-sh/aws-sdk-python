"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.import_job_id
    import aws_sdk_omics.types.sequence_store_id


class GetReadSetImportJobRequest(TypedDict):
    id: "aws_sdk_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadSetImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReadSetImportJobRequest:
    out: GetReadSetImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
