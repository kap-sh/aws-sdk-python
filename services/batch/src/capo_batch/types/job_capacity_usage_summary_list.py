"""Generated from Smithy shape ``com.amazonaws.batch#JobCapacityUsageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.job_capacity_usage_summary

JobCapacityUsageSummaryList: TypeAlias = list[
    "capo_batch.types.job_capacity_usage_summary.JobCapacityUsageSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobCapacityUsageSummaryList) -> list:
    import capo_batch.types.job_capacity_usage_summary

    out: list = []
    for item in value:
        out.append(capo_batch.types.job_capacity_usage_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobCapacityUsageSummaryList:
    import capo_batch.types.job_capacity_usage_summary

    out: JobCapacityUsageSummaryList = []
    for item in data:
        out.append(capo_batch.types.job_capacity_usage_summary.deserialize_json(item))
    return out
