"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousMaintenanceScheduleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

AutonomousMaintenanceScheduleType: TypeAlias = Literal[
    "EARLY",
    "REGULAR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EARLY",
        "REGULAR",
    )
)


def serialize_aws_json_1_0(value: AutonomousMaintenanceScheduleType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousMaintenanceScheduleType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutonomousMaintenanceScheduleType value: {data!r}"
        )
    return cast(AutonomousMaintenanceScheduleType, data)
