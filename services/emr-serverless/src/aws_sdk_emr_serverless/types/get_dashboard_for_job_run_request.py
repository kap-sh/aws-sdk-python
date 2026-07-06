"""Generated from Smithy shape ``com.amazonaws.emrserverless#GetDashboardForJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.attempt_number
    import aws_sdk_emr_serverless.types.job_run_id


class GetDashboardForJobRunRequest(TypedDict, closed=True):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    job_run_id: "aws_sdk_emr_serverless.types.job_run_id.JobRunId"
    """<p>The ID of the job run.</p>"""
    attempt: NotRequired["aws_sdk_emr_serverless.types.attempt_number.AttemptNumber"]
    """<p>An optimal parameter that indicates the amount of attempts for the job. If not specified, this value defaults to the attempt of the latest job.</p>"""
    access_system_profile_logs: NotRequired["bool"]
    """<p>Allows access to system profile logs for Lake Formation-enabled jobs. Default is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDashboardForJobRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDashboardForJobRunRequest:
    out: GetDashboardForJobRunRequest = {}  # type: ignore[typeddict-item]
    return out
