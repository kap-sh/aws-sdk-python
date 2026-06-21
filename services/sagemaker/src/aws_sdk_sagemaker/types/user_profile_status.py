"""Generated from Smithy shape ``com.amazonaws.sagemaker#UserProfileStatus``."""

from typing import Literal, TypeAlias, cast

UserProfileStatus: TypeAlias = Literal[
    "Deleting",
    "Failed",
    "InService",
    "Pending",
    "Updating",
    "Update_Failed",
    "Delete_Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserProfileStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserProfileStatus:
    return cast(UserProfileStatus, data)
