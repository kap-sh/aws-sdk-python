"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

ApplicationStatus: TypeAlias = Literal[
    "DELETING",
    "STARTING",
    "STOPPING",
    "READY",
    "RUNNING",
    "UPDATING",
    "AUTOSCALING",
    "FORCE_STOPPING",
    "ROLLING_BACK",
    "MAINTENANCE",
    "ROLLED_BACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETING",
        "STARTING",
        "STOPPING",
        "READY",
        "RUNNING",
        "UPDATING",
        "AUTOSCALING",
        "FORCE_STOPPING",
        "ROLLING_BACK",
        "MAINTENANCE",
        "ROLLED_BACK",
    )
)


def serialize_aws_json_1_1(value: ApplicationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatus value: {data!r}")
    return cast(ApplicationStatus, data)
