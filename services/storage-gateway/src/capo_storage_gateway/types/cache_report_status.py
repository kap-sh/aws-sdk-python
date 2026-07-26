"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportStatus``."""

from typing import Literal, TypeAlias, cast

CacheReportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "CANCELED",
    "FAILED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheReportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CacheReportStatus:
    return cast(CacheReportStatus, data)
