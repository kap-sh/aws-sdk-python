"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserImportJobStatusType``."""

from typing import Literal, TypeAlias, cast

UserImportJobStatusType: TypeAlias = Literal[
    "Created",
    "Pending",
    "InProgress",
    "Stopping",
    "Expired",
    "Stopped",
    "Failed",
    "Succeeded",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserImportJobStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserImportJobStatusType:
    return cast(UserImportJobStatusType, data)
