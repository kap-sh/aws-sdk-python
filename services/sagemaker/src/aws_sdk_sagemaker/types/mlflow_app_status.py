"""Generated from Smithy shape ``com.amazonaws.sagemaker#MlflowAppStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MlflowAppStatus: TypeAlias = Literal[
    "Creating",
    "Created",
    "CreateFailed",
    "Updating",
    "Updated",
    "UpdateFailed",
    "Deleting",
    "DeleteFailed",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Created",
        "CreateFailed",
        "Updating",
        "Updated",
        "UpdateFailed",
        "Deleting",
        "DeleteFailed",
        "Deleted",
    )
)


def serialize_aws_json_1_1(value: MlflowAppStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MlflowAppStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MlflowAppStatus value: {data!r}")
    return cast(MlflowAppStatus, data)
