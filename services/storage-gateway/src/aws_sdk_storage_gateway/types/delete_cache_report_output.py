"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteCacheReportOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cache_report_arn


class DeleteCacheReportOutput(TypedDict):
    cache_report_arn: NotRequired[
        "aws_sdk_storage_gateway.types.cache_report_arn.CacheReportARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the cache report you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCacheReportOutput) -> dict:
    out: dict = {}
    if "cache_report_arn" in value:
        out["CacheReportARN"] = value["cache_report_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCacheReportOutput:
    out: DeleteCacheReportOutput = {}  # type: ignore[typeddict-item]
    if "CacheReportARN" in data:
        out["cache_report_arn"] = data["CacheReportARN"]
    return out
