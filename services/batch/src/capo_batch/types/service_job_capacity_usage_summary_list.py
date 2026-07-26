"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobCapacityUsageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.service_job_capacity_usage_summary

ServiceJobCapacityUsageSummaryList: TypeAlias = list[
    "capo_batch.types.service_job_capacity_usage_summary.ServiceJobCapacityUsageSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobCapacityUsageSummaryList) -> list:
    import capo_batch.types.service_job_capacity_usage_summary

    out: list = []
    for item in value:
        out.append(
            capo_batch.types.service_job_capacity_usage_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceJobCapacityUsageSummaryList:
    import capo_batch.types.service_job_capacity_usage_summary

    out: ServiceJobCapacityUsageSummaryList = []
    for item in data:
        out.append(
            capo_batch.types.service_job_capacity_usage_summary.deserialize_json(item)
        )
    return out
