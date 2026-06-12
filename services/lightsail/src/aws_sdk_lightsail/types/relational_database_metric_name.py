"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

RelationalDatabaseMetricName: TypeAlias = Literal[
    "CPUUtilization",
    "DatabaseConnections",
    "DiskQueueDepth",
    "FreeStorageSpace",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPUUtilization",
        "DatabaseConnections",
        "DiskQueueDepth",
        "FreeStorageSpace",
        "NetworkReceiveThroughput",
        "NetworkTransmitThroughput",
    )
)


def serialize_aws_json_1_1(value: RelationalDatabaseMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationalDatabaseMetricName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RelationalDatabaseMetricName value: {data!r}"
        )
    return cast(RelationalDatabaseMetricName, data)
