"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalS3DataSourceDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AdditionalS3DataSourceDataType: TypeAlias = Literal[
    "S3Object",
    "S3Prefix",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3Object",
        "S3Prefix",
    )
)


def serialize_aws_json_1_1(value: AdditionalS3DataSourceDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdditionalS3DataSourceDataType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AdditionalS3DataSourceDataType value: {data!r}"
        )
    return cast(AdditionalS3DataSourceDataType, data)
