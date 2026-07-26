"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#JobIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.job_id

JobIds: TypeAlias = list["capo_compute_optimizer.types.job_id.JobId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: JobIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> JobIds:
    return list(data)
