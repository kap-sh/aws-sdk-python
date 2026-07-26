"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

MaintenanceWindowExecutionStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
    "TIMED_OUT",
    "CANCELLING",
    "CANCELLED",
    "SKIPPED_OVERLAPPING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceWindowExecutionStatus:
    return cast(MaintenanceWindowExecutionStatus, data)
