"""Generated from Smithy shape ``com.amazonaws.medicalimaging#StartDICOMImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.job_id
    import capo_medical_imaging.types.job_status


class StartDICOMImportJobResponse(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    job_id: "capo_medical_imaging.types.job_id.JobId"
    """<p>The import job identifier.</p>"""
    job_status: "capo_medical_imaging.types.job_status.JobStatus"
    """<p>The import job status.</p>"""
    submitted_at: "capo_medical_imaging.types.date.Date"
    """<p>The timestamp when the import job was submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDICOMImportJobResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["jobId"] = value["job_id"]
    import capo_medical_imaging.types.job_status

    out["jobStatus"] = capo_medical_imaging.types.job_status.serialize_json(
        value["job_status"]
    )
    import capo_medical_imaging.types.date

    out["submittedAt"] = capo_medical_imaging.types.date.serialize_json(
        value["submitted_at"]
    )
    return out


def deserialize_json(data: dict) -> StartDICOMImportJobResponse:
    out: StartDICOMImportJobResponse = {}  # type: ignore[typeddict-item]
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("StartDICOMImportJobResponse.datastore_id required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("StartDICOMImportJobResponse.job_id required")
    if "jobStatus" in data:
        import capo_medical_imaging.types.job_status

        out["job_status"] = capo_medical_imaging.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        raise DeserializationError("StartDICOMImportJobResponse.job_status required")
    if "submittedAt" in data:
        import capo_medical_imaging.types.date

        out["submitted_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["submittedAt"]
        )
    else:
        raise DeserializationError("StartDICOMImportJobResponse.submitted_at required")
    return out
