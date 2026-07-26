"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemStatus``."""

from typing import Literal, TypeAlias, cast

OpsItemStatus: TypeAlias = Literal[
    "Open",
    "InProgress",
    "Resolved",
    "Pending",
    "TimedOut",
    "Cancelling",
    "Cancelled",
    "Failed",
    "CompletedWithSuccess",
    "CompletedWithFailure",
    "Scheduled",
    "RunbookInProgress",
    "PendingChangeCalendarOverride",
    "ChangeCalendarOverrideApproved",
    "ChangeCalendarOverrideRejected",
    "PendingApproval",
    "Approved",
    "Revoked",
    "Rejected",
    "Closed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemStatus:
    return cast(OpsItemStatus, data)
