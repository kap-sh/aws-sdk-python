"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelPackageStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Completed",
    "Failed",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Completed",
        "Failed",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: ModelPackageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelPackageStatus value: {data!r}")
    return cast(ModelPackageStatus, data)
