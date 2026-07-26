"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.cache_report_info

CacheReportList: TypeAlias = list[
    "capo_storage_gateway.types.cache_report_info.CacheReportInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheReportList) -> list:
    import capo_storage_gateway.types.cache_report_info

    out: list = []
    for item in value:
        out.append(
            capo_storage_gateway.types.cache_report_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CacheReportList:
    import capo_storage_gateway.types.cache_report_info

    out: CacheReportList = []
    for item in data:
        out.append(
            capo_storage_gateway.types.cache_report_info.deserialize_aws_json_1_1(item)
        )
    return out
