"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetDICOMImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.job_id


class GetDICOMImportJobRequest(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    job_id: "capo_medical_imaging.types.job_id.JobId"
    """<p>The import job identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDICOMImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDICOMImportJobRequest:
    out: GetDICOMImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
