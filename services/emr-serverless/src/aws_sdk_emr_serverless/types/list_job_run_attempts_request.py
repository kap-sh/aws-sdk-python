"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListJobRunAttemptsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.job_run_id
    import aws_sdk_emr_serverless.types.next_token


class ListJobRunAttemptsRequest(TypedDict, closed=True):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application for which to list job runs.</p>"""
    job_run_id: "aws_sdk_emr_serverless.types.job_run_id.JobRunId"
    """<p>The ID of the job run to list.</p>"""
    next_token: NotRequired["aws_sdk_emr_serverless.types.next_token.NextToken"]
    """<p>The token for the next set of job run attempt results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of job run attempts to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobRunAttemptsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobRunAttemptsRequest:
    out: ListJobRunAttemptsRequest = {}  # type: ignore[typeddict-item]
    return out
