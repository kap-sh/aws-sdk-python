"""Generated from Smithy shape ``com.amazonaws.servicequotas#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "DEPENDENCY_ACCESS_DENIED_ERROR",
    "DEPENDENCY_THROTTLING_ERROR",
    "DEPENDENCY_SERVICE_ERROR",
    "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEPENDENCY_ACCESS_DENIED_ERROR",
        "DEPENDENCY_THROTTLING_ERROR",
        "DEPENDENCY_SERVICE_ERROR",
        "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
    )
)


def serialize_aws_json_1_1(value: ErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
