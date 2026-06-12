"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageGroupSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelPackageGroupSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: ModelPackageGroupSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageGroupSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelPackageGroupSortBy value: {data!r}")
    return cast(ModelPackageGroupSortBy, data)
