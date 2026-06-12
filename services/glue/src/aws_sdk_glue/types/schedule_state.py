"""Generated from Smithy shape ``com.amazonaws.glue#ScheduleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ScheduleState: TypeAlias = Literal[
    "SCHEDULED",
    "NOT_SCHEDULED",
    "TRANSITIONING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "NOT_SCHEDULED",
        "TRANSITIONING",
    )
)


def serialize_aws_json_1_1(value: ScheduleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduleState value: {data!r}")
    return cast(ScheduleState, data)
