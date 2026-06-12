"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListJobRunsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.job_runs
    import aws_sdk_emr_serverless.types.next_token


class ListJobRunsResponse(TypedDict):
    job_runs: "aws_sdk_emr_serverless.types.job_runs.JobRuns"
    """<p>The output lists information about the specified job runs.</p>"""
    next_token: NotRequired["aws_sdk_emr_serverless.types.next_token.NextToken"]
    """<p>The output displays the token for the next set of job run results. This is required for pagination and is available as a response of the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunsResponse) -> dict:
    out: dict = {}
    import aws_sdk_emr_serverless.types.job_runs

    out["jobRuns"] = aws_sdk_emr_serverless.types.job_runs.serialize_json(
        value["job_runs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobRunsResponse:
    out: ListJobRunsResponse = {}  # type: ignore[typeddict-item]
    if "jobRuns" in data:
        import aws_sdk_emr_serverless.types.job_runs

        out["job_runs"] = aws_sdk_emr_serverless.types.job_runs.deserialize_json(
            data["jobRuns"]
        )
    else:
        raise DeserializationError("ListJobRunsResponse.job_runs required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
