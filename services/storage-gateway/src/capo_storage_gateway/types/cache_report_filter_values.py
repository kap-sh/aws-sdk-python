"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.cache_report_filter_value

CacheReportFilterValues: TypeAlias = list[
    "capo_storage_gateway.types.cache_report_filter_value.CacheReportFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheReportFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CacheReportFilterValues:
    return list(data)
