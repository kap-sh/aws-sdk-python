"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobCapacityUsageDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.service_job_capacity_usage_detail

ServiceJobCapacityUsageDetailList: TypeAlias = list[
    "aws_sdk_batch.types.service_job_capacity_usage_detail.ServiceJobCapacityUsageDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobCapacityUsageDetailList) -> list:
    import aws_sdk_batch.types.service_job_capacity_usage_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_batch.types.service_job_capacity_usage_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceJobCapacityUsageDetailList:
    import aws_sdk_batch.types.service_job_capacity_usage_detail

    out: ServiceJobCapacityUsageDetailList = []
    for item in data:
        out.append(
            aws_sdk_batch.types.service_job_capacity_usage_detail.deserialize_json(item)
        )
    return out
