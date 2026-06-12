"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeCacheReportOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cache_report_info


class DescribeCacheReportOutput(TypedDict):
    cache_report_info: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_info.CacheReportInfo"
    ]
    """<p>Contains all informational fields associated with a cache report. Includes name, ARN, tags, status, progress, filters, start time, and end time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCacheReportOutput) -> dict:
    out: dict = {}
    if "cache_report_info" in value:
        import aws_sdk_storage_gateway.types.cache_report_info

        out["CacheReportInfo"] = (
            aws_sdk_storage_gateway.types.cache_report_info.serialize_aws_json_1_1(
                value["cache_report_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCacheReportOutput:
    out: DescribeCacheReportOutput = {}  # type: ignore[typeddict-item]
    if "CacheReportInfo" in data:
        import aws_sdk_storage_gateway.types.cache_report_info

        out["cache_report_info"] = (
            aws_sdk_storage_gateway.types.cache_report_info.deserialize_aws_json_1_1(
                data["CacheReportInfo"]
            )
        )
    return out
