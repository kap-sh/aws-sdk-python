"""Generated from Smithy shape ``com.amazonaws.batch#JobStateTimeLimitActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.job_state_time_limit_action

JobStateTimeLimitActions: TypeAlias = list[
    "aws_sdk_batch.types.job_state_time_limit_action.JobStateTimeLimitAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStateTimeLimitActions) -> list:
    import aws_sdk_batch.types.job_state_time_limit_action

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.job_state_time_limit_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobStateTimeLimitActions:
    import aws_sdk_batch.types.job_state_time_limit_action

    out: JobStateTimeLimitActions = []
    for item in data:
        out.append(
            aws_sdk_batch.types.job_state_time_limit_action.deserialize_json(item)
        )
    return out
