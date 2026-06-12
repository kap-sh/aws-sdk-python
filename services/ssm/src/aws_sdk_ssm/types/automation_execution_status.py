"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AutomationExecutionStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Waiting",
    "Success",
    "TimedOut",
    "Cancelling",
    "Cancelled",
    "Failed",
    "PendingApproval",
    "Approved",
    "Rejected",
    "Scheduled",
    "RunbookInProgress",
    "PendingChangeCalendarOverride",
    "ChangeCalendarOverrideApproved",
    "ChangeCalendarOverrideRejected",
    "CompletedWithSuccess",
    "CompletedWithFailure",
    "Exited",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Waiting",
        "Success",
        "TimedOut",
        "Cancelling",
        "Cancelled",
        "Failed",
        "PendingApproval",
        "Approved",
        "Rejected",
        "Scheduled",
        "RunbookInProgress",
        "PendingChangeCalendarOverride",
        "ChangeCalendarOverrideApproved",
        "ChangeCalendarOverrideRejected",
        "CompletedWithSuccess",
        "CompletedWithFailure",
        "Exited",
    )
)


def serialize_aws_json_1_1(value: AutomationExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomationExecutionStatus value: {data!r}")
    return cast(AutomationExecutionStatus, data)
