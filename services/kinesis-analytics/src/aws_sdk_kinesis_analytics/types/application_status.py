"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics.errors import DeserializationError

ApplicationStatus: TypeAlias = Literal[
    "DELETING",
    "STARTING",
    "STOPPING",
    "READY",
    "RUNNING",
    "UPDATING",
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
    )
)


def serialize_aws_json_1_1(value: ApplicationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatus value: {data!r}")
    return cast(ApplicationStatus, data)
