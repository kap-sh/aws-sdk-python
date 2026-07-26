"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.export_job_id
    import capo_omics.types.sequence_store_id


class GetReadSetExportJobRequest(TypedDict, closed=True):
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""
    id: "capo_omics.types.export_job_id.ExportJobId"
    """<p>The job's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadSetExportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReadSetExportJobRequest:
    out: GetReadSetExportJobRequest = {}  # type: ignore[typeddict-item]
    return out
