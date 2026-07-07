"""Generated from Smithy shape ``com.amazonaws.healthlake#StartFHIRExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.datastore_id
    import aws_sdk_healthlake.types.job_id
    import aws_sdk_healthlake.types.job_status


class StartFHIRExportJobResponse(TypedDict, closed=True):
    job_id: "aws_sdk_healthlake.types.job_id.JobId"
    """<p>The export job identifier.</p>"""
    job_status: "aws_sdk_healthlake.types.job_status.JobStatus"
    """<p>The export job status.</p>"""
    datastore_id: NotRequired["aws_sdk_healthlake.types.datastore_id.DatastoreId"]
    """<p>The data store identifier from which files are being exported.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFHIRExportJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    import aws_sdk_healthlake.types.job_status

    out["JobStatus"] = aws_sdk_healthlake.types.job_status.serialize_aws_json_1_0(
        value["job_status"]
    )
    if "datastore_id" in value:
        out["DatastoreId"] = value["datastore_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFHIRExportJobResponse:
    out: StartFHIRExportJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("StartFHIRExportJobResponse.job_id required")
    if "JobStatus" in data:
        import aws_sdk_healthlake.types.job_status

        out["job_status"] = (
            aws_sdk_healthlake.types.job_status.deserialize_aws_json_1_0(
                data["JobStatus"]
            )
        )
    else:
        raise DeserializationError("StartFHIRExportJobResponse.job_status required")
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    return out
