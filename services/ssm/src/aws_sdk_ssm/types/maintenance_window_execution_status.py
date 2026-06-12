"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
        "TIMED_OUT",
        "CANCELLING",
        "CANCELLED",
        "SKIPPED_OVERLAPPING",
    )
)


def serialize_aws_json_1_1(value: MaintenanceWindowExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceWindowExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MaintenanceWindowExecutionStatus value: {data!r}"
        )
    return cast(MaintenanceWindowExecutionStatus, data)
