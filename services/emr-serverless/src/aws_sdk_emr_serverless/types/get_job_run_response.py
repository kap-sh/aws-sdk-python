"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetJobRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.job_run


class GetJobRunResponse(TypedDict):
    job_run: "aws_sdk_emr_serverless.types.job_run.JobRun"
    """<p>The output displays information about the job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobRunResponse) -> dict:
    out: dict = {}
    import aws_sdk_emr_serverless.types.job_run

    out["jobRun"] = aws_sdk_emr_serverless.types.job_run.serialize_json(
        value["job_run"]
    )
    return out


def deserialize_json(data: dict) -> GetJobRunResponse:
    out: GetJobRunResponse = {}  # type: ignore[typeddict-item]
    if "jobRun" in data:
        import aws_sdk_emr_serverless.types.job_run

        out["job_run"] = aws_sdk_emr_serverless.types.job_run.deserialize_json(
            data["jobRun"]
        )
    else:
        raise DeserializationError("GetJobRunResponse.job_run required")
    return out
