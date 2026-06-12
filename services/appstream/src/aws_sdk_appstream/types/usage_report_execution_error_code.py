"""Generated from Smithy shape ``com.amazonaws.appstream#UsageReportExecutionErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

UsageReportExecutionErrorCode: TypeAlias = Literal[
    "RESOURCE_NOT_FOUND",
    "ACCESS_DENIED",
    "INTERNAL_SERVICE_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE_NOT_FOUND",
        "ACCESS_DENIED",
        "INTERNAL_SERVICE_ERROR",
    )
)


def serialize_aws_json_1_1(value: UsageReportExecutionErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsageReportExecutionErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UsageReportExecutionErrorCode value: {data!r}"
        )
    return cast(UsageReportExecutionErrorCode, data)
