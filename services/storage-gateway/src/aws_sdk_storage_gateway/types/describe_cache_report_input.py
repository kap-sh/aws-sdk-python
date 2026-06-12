"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeCacheReportInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.cache_report_arn


class DescribeCacheReportInput(TypedDict):
    cache_report_arn: "aws_sdk_storage_gateway.types.cache_report_arn.CacheReportARN"
    """<p>The Amazon Resource Name (ARN) of the cache report you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCacheReportInput) -> dict:
    out: dict = {}
    out["CacheReportARN"] = value["cache_report_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCacheReportInput:
    out: DescribeCacheReportInput = {}  # type: ignore[typeddict-item]
    if "CacheReportARN" in data:
        out["cache_report_arn"] = data["CacheReportARN"]
    else:
        raise DeserializationError("DescribeCacheReportInput.cache_report_arn required")
    return out
