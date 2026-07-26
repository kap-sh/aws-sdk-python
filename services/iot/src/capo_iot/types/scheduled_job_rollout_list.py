"""Generated from Smithy shape ``com.amazonaws.iot#ScheduledJobRolloutList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.scheduled_job_rollout

ScheduledJobRolloutList: TypeAlias = list[
    "capo_iot.types.scheduled_job_rollout.ScheduledJobRollout"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledJobRolloutList) -> list:
    import capo_iot.types.scheduled_job_rollout

    out: list = []
    for item in value:
        out.append(capo_iot.types.scheduled_job_rollout.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScheduledJobRolloutList:
    import capo_iot.types.scheduled_job_rollout

    out: ScheduledJobRolloutList = []
    for item in data:
        out.append(capo_iot.types.scheduled_job_rollout.deserialize_json(item))
    return out
