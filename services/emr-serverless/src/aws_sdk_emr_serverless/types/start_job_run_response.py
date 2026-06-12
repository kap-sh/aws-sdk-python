"""Generated from Smithy shape ``com.amazonaws.emrserverless#StartJobRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.job_arn
    import aws_sdk_emr_serverless.types.job_run_id


class StartJobRunResponse(TypedDict):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>This output displays the application ID on which the job run was submitted.</p>"""
    job_run_id: "aws_sdk_emr_serverless.types.job_run_id.JobRunId"
    """<p>The output contains the ID of the started job run.</p>"""
    arn: "aws_sdk_emr_serverless.types.job_arn.JobArn"
    """<p>This output displays the ARN of the job run..</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRunResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["jobRunId"] = value["job_run_id"]
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StartJobRunResponse:
    out: StartJobRunResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("StartJobRunResponse.application_id required")
    if "jobRunId" in data:
        out["job_run_id"] = data["jobRunId"]
    else:
        raise DeserializationError("StartJobRunResponse.job_run_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("StartJobRunResponse.arn required")
    return out
