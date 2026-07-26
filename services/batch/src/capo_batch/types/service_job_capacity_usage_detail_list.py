"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobCapacityUsageDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.service_job_capacity_usage_detail

ServiceJobCapacityUsageDetailList: TypeAlias = list[
    "capo_batch.types.service_job_capacity_usage_detail.ServiceJobCapacityUsageDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobCapacityUsageDetailList) -> list:
    import capo_batch.types.service_job_capacity_usage_detail

    out: list = []
    for item in value:
        out.append(
            capo_batch.types.service_job_capacity_usage_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceJobCapacityUsageDetailList:
    import capo_batch.types.service_job_capacity_usage_detail

    out: ServiceJobCapacityUsageDetailList = []
    for item in data:
        out.append(
            capo_batch.types.service_job_capacity_usage_detail.deserialize_json(item)
        )
    return out
