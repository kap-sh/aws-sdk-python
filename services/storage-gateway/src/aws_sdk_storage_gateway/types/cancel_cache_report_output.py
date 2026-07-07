"""Generated from Smithy shape ``com.amazonaws.storagegateway#CancelCacheReportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cache_report_arn


class CancelCacheReportOutput(TypedDict, closed=True):
    cache_report_arn: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_arn.CacheReportARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the cache report you want to cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelCacheReportOutput) -> dict:
    out: dict = {}
    if "cache_report_arn" in value:
        out["CacheReportARN"] = value["cache_report_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelCacheReportOutput:
    out: CancelCacheReportOutput = {}  # type: ignore[typeddict-item]
    if "CacheReportARN" in data:
        out["cache_report_arn"] = data["CacheReportARN"]
    return out
