"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ScheduleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_dashboards.errors import DeserializationError

ScheduleState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: ScheduleState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScheduleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduleState value: {data!r}")
    return cast(ScheduleState, data)
