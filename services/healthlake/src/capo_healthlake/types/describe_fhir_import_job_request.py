"""Generated from Smithy shape ``com.amazonaws.healthlake#DescribeFHIRImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.job_id


class DescribeFHIRImportJobRequest(TypedDict, closed=True):
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    job_id: "capo_healthlake.types.job_id.JobId"
    """<p>The import job identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFHIRImportJobRequest) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFHIRImportJobRequest:
    out: DescribeFHIRImportJobRequest = {}  # type: ignore[typeddict-item]
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("DescribeFHIRImportJobRequest.datastore_id required")
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("DescribeFHIRImportJobRequest.job_id required")
    return out
