"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#S3TableIntegrationSourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

S3TableIntegrationSourceStatus: TypeAlias = Literal[
    "ACTIVE",
    "UNHEALTHY",
    "FAILED",
    "DATA_SOURCE_DELETE_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "UNHEALTHY",
        "FAILED",
        "DATA_SOURCE_DELETE_IN_PROGRESS",
    )
)


def serialize_aws_json_1_1(value: S3TableIntegrationSourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3TableIntegrationSourceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown S3TableIntegrationSourceStatus value: {data!r}"
        )
    return cast(S3TableIntegrationSourceStatus, data)
