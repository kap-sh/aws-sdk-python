"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3ModelDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

S3ModelDataType: TypeAlias = Literal[
    "S3Prefix",
    "S3Object",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3Prefix",
        "S3Object",
    )
)


def serialize_aws_json_1_1(value: S3ModelDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3ModelDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3ModelDataType value: {data!r}")
    return cast(S3ModelDataType, data)
