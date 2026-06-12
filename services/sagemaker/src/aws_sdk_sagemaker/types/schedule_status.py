"""Generated from Smithy shape ``com.amazonaws.sagemaker#ScheduleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ScheduleStatus: TypeAlias = Literal[
    "Pending",
    "Failed",
    "Scheduled",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Failed",
        "Scheduled",
        "Stopped",
    )
)


def serialize_aws_json_1_1(value: ScheduleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduleStatus value: {data!r}")
    return cast(ScheduleStatus, data)
