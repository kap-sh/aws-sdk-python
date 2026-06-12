"""Generated from Smithy shape ``com.amazonaws.datasync#ScheduleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

ScheduleStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ScheduleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduleStatus value: {data!r}")
    return cast(ScheduleStatus, data)
