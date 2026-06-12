"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobRunStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.job_run_state

JobRunStates: TypeAlias = list["aws_sdk_emr_containers.types.job_run_state.JobRunState"]


# --- restJson1 ser/de ---
def serialize_json(value: JobRunStates) -> list:
    import aws_sdk_emr_containers.types.job_run_state

    out: list = []
    for item in value:
        out.append(aws_sdk_emr_containers.types.job_run_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobRunStates:
    import aws_sdk_emr_containers.types.job_run_state

    out: JobRunStates = []
    for item in data:
        out.append(aws_sdk_emr_containers.types.job_run_state.deserialize_json(item))
    return out
