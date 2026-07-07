"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobPreemptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.service_job_recent_preempted_attempt_list


class ServiceJobPreemptionSummary(TypedDict, closed=True):
    preempted_attempt_count: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The total number of times the service job has been preempted.</p>"""
    recent_preempted_attempts: NotRequired[
        "aws_sdk_batch.types.service_job_recent_preempted_attempt_list.ServiceJobRecentPreemptedAttemptList"
    ]
    """<p>A list of the most recent preemption attempts for the service job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobPreemptionSummary) -> dict:
    out: dict = {}
    if "preempted_attempt_count" in value:
        out["preemptedAttemptCount"] = value["preempted_attempt_count"]
    if "recent_preempted_attempts" in value:
        import aws_sdk_batch.types.service_job_recent_preempted_attempt_list

        out["recentPreemptedAttempts"] = (
            aws_sdk_batch.types.service_job_recent_preempted_attempt_list.serialize_json(
                value["recent_preempted_attempts"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceJobPreemptionSummary:
    out: ServiceJobPreemptionSummary = {}  # type: ignore[typeddict-item]
    if "preemptedAttemptCount" in data:
        out["preempted_attempt_count"] = data["preemptedAttemptCount"]
    if "recentPreemptedAttempts" in data:
        import aws_sdk_batch.types.service_job_recent_preempted_attempt_list

        out["recent_preempted_attempts"] = (
            aws_sdk_batch.types.service_job_recent_preempted_attempt_list.deserialize_json(
                data["recentPreemptedAttempts"]
            )
        )
    return out
