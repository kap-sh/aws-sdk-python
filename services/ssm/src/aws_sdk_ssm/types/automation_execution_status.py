"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: AutomationExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationExecutionStatus:
    return cast(AutomationExecutionStatus, data)
