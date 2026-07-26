"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportFilterName``."""

from typing import Literal, TypeAlias, cast

CacheReportFilterName: TypeAlias = Literal[
    "UploadState",
    "UploadFailureReason",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheReportFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CacheReportFilterName:
    return cast(CacheReportFilterName, data)
