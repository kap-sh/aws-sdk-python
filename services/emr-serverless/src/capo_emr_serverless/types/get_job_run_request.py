"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.attempt_number
    import capo_emr_serverless.types.job_run_id


class GetJobRunRequest(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application on which the job run is submitted.</p>"""
    job_run_id: "capo_emr_serverless.types.job_run_id.JobRunId"
    """<p>The ID of the job run.</p>"""
    attempt: NotRequired["capo_emr_serverless.types.attempt_number.AttemptNumber"]
    """<p>An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJobRunRequest:
    out: GetJobRunRequest = {}  # type: ignore[typeddict-item]
    return out
