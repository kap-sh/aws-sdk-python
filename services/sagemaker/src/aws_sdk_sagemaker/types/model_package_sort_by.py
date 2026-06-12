"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelPackageSortBy: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ModelPackageSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelPackageSortBy value: {data!r}")
    return cast(ModelPackageSortBy, data)
