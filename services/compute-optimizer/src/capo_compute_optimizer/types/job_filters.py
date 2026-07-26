"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#JobFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.job_filter

JobFilters: TypeAlias = list["capo_compute_optimizer.types.job_filter.JobFilter"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: JobFilters) -> list:
    import capo_compute_optimizer.types.job_filter

    out: list = []
    for item in value:
        out.append(capo_compute_optimizer.types.job_filter.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> JobFilters:
    import capo_compute_optimizer.types.job_filter

    out: JobFilters = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.job_filter.deserialize_aws_json_1_0(item)
        )
    return out
