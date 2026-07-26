"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.date_type
    import capo_iot.types.execution_number
    import capo_iot.types.job_execution_status
    import capo_iot.types.retry_attempt


class JobExecutionSummary(TypedDict, closed=True):
    status: NotRequired["capo_iot.types.job_execution_status.JobExecutionStatus"]
    """<p>The status of the job execution.</p>"""
    queued_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job execution was queued.</p>"""
    started_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job execution started.</p>"""
    last_updated_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job execution was last updated.</p>"""
    execution_number: NotRequired["capo_iot.types.execution_number.ExecutionNumber"]
    r"""<p>A string (consisting of the digits \"0\" through \"9\") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.</p>"""
    retry_attempt: NotRequired["capo_iot.types.retry_attempt.RetryAttempt"]
    """<p>The number that indicates how many retry attempts have been completed for this job on this device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionSummary) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_iot.types.job_execution_status

        out["status"] = capo_iot.types.job_execution_status.serialize_json(
            value["status"]
        )
    if "queued_at" in value:
        import capo_iot.types.date_type

        out["queuedAt"] = capo_iot.types.date_type.serialize_json(value["queued_at"])
    if "started_at" in value:
        import capo_iot.types.date_type

        out["startedAt"] = capo_iot.types.date_type.serialize_json(value["started_at"])
    if "last_updated_at" in value:
        import capo_iot.types.date_type

        out["lastUpdatedAt"] = capo_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    if "execution_number" in value:
        out["executionNumber"] = value["execution_number"]
    if "retry_attempt" in value:
        out["retryAttempt"] = value["retry_attempt"]
    return out


def deserialize_json(data: dict) -> JobExecutionSummary:
    out: JobExecutionSummary = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_iot.types.job_execution_status

        out["status"] = capo_iot.types.job_execution_status.deserialize_json(
            data["status"]
        )
    if "queuedAt" in data:
        import capo_iot.types.date_type

        out["queued_at"] = capo_iot.types.date_type.deserialize_json(data["queuedAt"])
    if "startedAt" in data:
        import capo_iot.types.date_type

        out["started_at"] = capo_iot.types.date_type.deserialize_json(data["startedAt"])
    if "lastUpdatedAt" in data:
        import capo_iot.types.date_type

        out["last_updated_at"] = capo_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "executionNumber" in data:
        out["execution_number"] = data["executionNumber"]
    if "retryAttempt" in data:
        out["retry_attempt"] = data["retryAttempt"]
    return out
