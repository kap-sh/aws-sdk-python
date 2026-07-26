"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReceivedStatus``."""

from typing import Literal, TypeAlias, cast

ReceivedStatus: TypeAlias = Literal[
    "PENDING_WORKFLOW",
    "PENDING_ACCEPT",
    "REJECTED",
    "ACTIVE",
    "FAILED_WORKFLOW",
    "DELETED",
    "DISABLED",
    "WORKFLOW_COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReceivedStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReceivedStatus:
    return cast(ReceivedStatus, data)
