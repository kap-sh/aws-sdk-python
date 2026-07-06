"""Generated from Smithy shape ``com.amazonaws.emrserverless#CancelJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.job_run_id
    import aws_sdk_emr_serverless.types.shutdown_grace_period_in_seconds


class CancelJobRunRequest(TypedDict, closed=True):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application on which the job run will be canceled.</p>"""
    job_run_id: "aws_sdk_emr_serverless.types.job_run_id.JobRunId"
    """<p>The ID of the job run to cancel.</p>"""
    shutdown_grace_period_in_seconds: NotRequired[
        "aws_sdk_emr_serverless.types.shutdown_grace_period_in_seconds.ShutdownGracePeriodInSeconds"
    ]
    """<p>The duration in seconds to wait before forcefully terminating the job after cancellation is requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelJobRunRequest:
    out: CancelJobRunRequest = {}  # type: ignore[typeddict-item]
    return out
