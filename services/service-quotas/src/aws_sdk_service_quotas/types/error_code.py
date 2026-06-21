"""Generated from Smithy shape ``com.amazonaws.servicequotas#ErrorCode``."""

from typing import Literal, TypeAlias, cast

ErrorCode: TypeAlias = Literal[
    "DEPENDENCY_ACCESS_DENIED_ERROR",
    "DEPENDENCY_THROTTLING_ERROR",
    "DEPENDENCY_SERVICE_ERROR",
    "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
