"""Generated from Smithy shape ``com.amazonaws.emrserverless#CancelJobRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.job_run_id


class CancelJobRunResponse(TypedDict):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The output contains the application ID on which the job run is cancelled.</p>"""
    job_run_id: "aws_sdk_emr_serverless.types.job_run_id.JobRunId"
    """<p>The output contains the ID of the cancelled job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRunResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["jobRunId"] = value["job_run_id"]
    return out


def deserialize_json(data: dict) -> CancelJobRunResponse:
    out: CancelJobRunResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("CancelJobRunResponse.application_id required")
    if "jobRunId" in data:
        out["job_run_id"] = data["jobRunId"]
    else:
        raise DeserializationError("CancelJobRunResponse.job_run_id required")
    return out
