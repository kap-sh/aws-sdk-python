"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobAttemptDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.service_job_attempt_detail

ServiceJobAttemptDetails: TypeAlias = list[
    "capo_batch.types.service_job_attempt_detail.ServiceJobAttemptDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobAttemptDetails) -> list:
    import capo_batch.types.service_job_attempt_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.service_job_attempt_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceJobAttemptDetails:
    import capo_batch.types.service_job_attempt_detail

    out: ServiceJobAttemptDetails = []
    for item in data:
        out.append(capo_batch.types.service_job_attempt_detail.deserialize_json(item))
    return out
