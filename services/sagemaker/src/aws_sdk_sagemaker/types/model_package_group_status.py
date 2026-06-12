"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelPackageGroupStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Completed",
    "Failed",
    "Deleting",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Completed",
        "Failed",
        "Deleting",
        "DeleteFailed",
    )
)


def serialize_aws_json_1_1(value: ModelPackageGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelPackageGroupStatus value: {data!r}")
    return cast(ModelPackageGroupStatus, data)
