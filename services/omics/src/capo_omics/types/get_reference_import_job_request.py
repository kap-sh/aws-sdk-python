"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.import_job_id
    import capo_omics.types.reference_store_id


class GetReferenceImportJobRequest(TypedDict, closed=True):
    id: "capo_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The job's reference store ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReferenceImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReferenceImportJobRequest:
    out: GetReferenceImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
