"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseManagementStatus``."""

from typing import Literal, TypeAlias, cast

DatabaseManagementStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "NOT_ENABLED",
    "FAILED_ENABLING",
    "FAILED_DISABLING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseManagementStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatabaseManagementStatus:
    return cast(DatabaseManagementStatus, data)
