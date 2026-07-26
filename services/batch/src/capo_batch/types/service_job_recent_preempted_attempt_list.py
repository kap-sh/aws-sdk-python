"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobRecentPreemptedAttemptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.service_job_preempted_attempt

ServiceJobRecentPreemptedAttemptList: TypeAlias = list[
    "capo_batch.types.service_job_preempted_attempt.ServiceJobPreemptedAttempt"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobRecentPreemptedAttemptList) -> list:
    import capo_batch.types.service_job_preempted_attempt

    out: list = []
    for item in value:
        out.append(capo_batch.types.service_job_preempted_attempt.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceJobRecentPreemptedAttemptList:
    import capo_batch.types.service_job_preempted_attempt

    out: ServiceJobRecentPreemptedAttemptList = []
    for item in data:
        out.append(
            capo_batch.types.service_job_preempted_attempt.deserialize_json(item)
        )
    return out
