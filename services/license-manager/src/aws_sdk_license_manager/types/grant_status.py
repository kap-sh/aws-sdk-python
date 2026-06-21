"""Generated from Smithy shape ``com.amazonaws.licensemanager#GrantStatus``."""

from typing import Literal, TypeAlias, cast

GrantStatus: TypeAlias = Literal[
    "PENDING_WORKFLOW",
    "PENDING_ACCEPT",
    "REJECTED",
    "ACTIVE",
    "FAILED_WORKFLOW",
    "DELETED",
    "PENDING_DELETE",
    "DISABLED",
    "WORKFLOW_COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GrantStatus:
    return cast(GrantStatus, data)
