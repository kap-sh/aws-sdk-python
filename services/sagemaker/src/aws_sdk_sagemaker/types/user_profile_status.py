"""Generated from Smithy shape ``com.amazonaws.sagemaker#UserProfileStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Deleting",
        "Failed",
        "InService",
        "Pending",
        "Updating",
        "Update_Failed",
        "Delete_Failed",
    )
)


def serialize_aws_json_1_1(value: UserProfileStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserProfileStatus value: {data!r}")
    return cast(UserProfileStatus, data)
