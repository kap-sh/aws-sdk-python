"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

DeliverySourceStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: DeliverySourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliverySourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliverySourceStatus value: {data!r}")
    return cast(DeliverySourceStatus, data)
