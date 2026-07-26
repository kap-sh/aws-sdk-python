"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.cache_report_filter

CacheReportFilterList: TypeAlias = list[
    "capo_storage_gateway.types.cache_report_filter.CacheReportFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheReportFilterList) -> list:
    import capo_storage_gateway.types.cache_report_filter

    out: list = []
    for item in value:
        out.append(
            capo_storage_gateway.types.cache_report_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CacheReportFilterList:
    import capo_storage_gateway.types.cache_report_filter

    out: CacheReportFilterList = []
    for item in data:
        out.append(
            capo_storage_gateway.types.cache_report_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
