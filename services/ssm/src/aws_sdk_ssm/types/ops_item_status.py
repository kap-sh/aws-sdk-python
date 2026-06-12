"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: OpsItemStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsItemStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpsItemStatus value: {data!r}")
    return cast(OpsItemStatus, data)
