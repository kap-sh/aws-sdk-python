"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobRuns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.job_run

JobRuns: TypeAlias = list["aws_sdk_emr_containers.types.job_run.JobRun"]


# --- restJson1 ser/de ---
def serialize_json(value: JobRuns) -> list:
    import aws_sdk_emr_containers.types.job_run

    out: list = []
    for item in value:
        out.append(aws_sdk_emr_containers.types.job_run.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobRuns:
    import aws_sdk_emr_containers.types.job_run

    out: JobRuns = []
    for item in data:
        out.append(aws_sdk_emr_containers.types.job_run.deserialize_json(item))
    return out
