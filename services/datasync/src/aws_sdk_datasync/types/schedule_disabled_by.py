"""Generated from Smithy shape ``com.amazonaws.datasync#ScheduleDisabledBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

ScheduleDisabledBy: TypeAlias = Literal[
    "USER",
    "SERVICE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "SERVICE",
    )
)


def serialize_aws_json_1_1(value: ScheduleDisabledBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleDisabledBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduleDisabledBy value: {data!r}")
    return cast(ScheduleDisabledBy, data)
