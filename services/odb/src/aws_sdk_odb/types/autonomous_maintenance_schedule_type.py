"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousMaintenanceScheduleType``."""

from typing import Literal, TypeAlias, cast

AutonomousMaintenanceScheduleType: TypeAlias = Literal[
    "EARLY",
    "REGULAR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousMaintenanceScheduleType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousMaintenanceScheduleType:
    return cast(AutonomousMaintenanceScheduleType, data)
