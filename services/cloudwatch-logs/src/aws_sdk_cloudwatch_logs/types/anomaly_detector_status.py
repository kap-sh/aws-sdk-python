"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AnomalyDetectorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

AnomalyDetectorStatus: TypeAlias = Literal[
    "INITIALIZING",
    "TRAINING",
    "ANALYZING",
    "FAILED",
    "DELETED",
    "PAUSED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZING",
        "TRAINING",
        "ANALYZING",
        "FAILED",
        "DELETED",
        "PAUSED",
    )
)


def serialize_aws_json_1_1(value: AnomalyDetectorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnomalyDetectorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnomalyDetectorStatus value: {data!r}")
    return cast(AnomalyDetectorStatus, data)
