"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

ExecutionState: TypeAlias = Literal[
    "inProgress",
    "pausedByFailedStep",
    "pausedByOperator",
    "completed",
    "completedWithExceptions",
    "canceled",
    "planExecutionTimedOut",
    "pendingManualApproval",
    "failed",
    "pending",
    "completedMonitoringApplicationHealth",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "inProgress",
        "pausedByFailedStep",
        "pausedByOperator",
        "completed",
        "completedWithExceptions",
        "canceled",
        "planExecutionTimedOut",
        "pendingManualApproval",
        "failed",
        "pending",
        "completedMonitoringApplicationHealth",
    )
)


def serialize_aws_json_1_0(value: ExecutionState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionState value: {data!r}")
    return cast(ExecutionState, data)
