"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetadataFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelMetadataFilterType: TypeAlias = Literal[
    "Domain",
    "Framework",
    "Task",
    "FrameworkVersion",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Domain",
        "Framework",
        "Task",
        "FrameworkVersion",
    )
)


def serialize_aws_json_1_1(value: ModelMetadataFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelMetadataFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelMetadataFilterType value: {data!r}")
    return cast(ModelMetadataFilterType, data)
