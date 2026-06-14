"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

IntegrationStatus: TypeAlias = Literal[
    "PROVISIONING",
    "ACTIVE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING",
        "ACTIVE",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: IntegrationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IntegrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationStatus value: {data!r}")
    return cast(IntegrationStatus, data)
