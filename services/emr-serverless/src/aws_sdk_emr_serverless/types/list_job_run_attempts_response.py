"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListJobRunAttemptsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.job_run_attempts
    import aws_sdk_emr_serverless.types.next_token


class ListJobRunAttemptsResponse(TypedDict):
    job_run_attempts: "aws_sdk_emr_serverless.types.job_run_attempts.JobRunAttempts"
    """<p>The array of the listed job run attempt objects.</p>"""
    next_token: NotRequired["aws_sdk_emr_serverless.types.next_token.NextToken"]
    """<p>The output displays the token for the next set of application results. This is required for pagination and is available as a response of the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunAttemptsResponse) -> dict:
    out: dict = {}
    import aws_sdk_emr_serverless.types.job_run_attempts

    out["jobRunAttempts"] = (
        aws_sdk_emr_serverless.types.job_run_attempts.serialize_json(
            value["job_run_attempts"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobRunAttemptsResponse:
    out: ListJobRunAttemptsResponse = {}  # type: ignore[typeddict-item]
    if "jobRunAttempts" in data:
        import aws_sdk_emr_serverless.types.job_run_attempts

        out["job_run_attempts"] = (
            aws_sdk_emr_serverless.types.job_run_attempts.deserialize_json(
                data["jobRunAttempts"]
            )
        )
    else:
        raise DeserializationError(
            "ListJobRunAttemptsResponse.job_run_attempts required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
