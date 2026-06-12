"""Generated from Smithy shape ``com.amazonaws.glue#ScheduleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ScheduleType: TypeAlias = Literal[
    "CRON",
    "AUTO",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRON",
        "AUTO",
    )
)


def serialize_aws_json_1_1(value: ScheduleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduleType value: {data!r}")
    return cast(ScheduleType, data)
