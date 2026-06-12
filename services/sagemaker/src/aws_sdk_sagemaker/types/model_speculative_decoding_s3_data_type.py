"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSpeculativeDecodingS3DataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelSpeculativeDecodingS3DataType: TypeAlias = Literal[
    "S3Prefix",
    "ManifestFile",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3Prefix",
        "ManifestFile",
    )
)


def serialize_aws_json_1_1(value: ModelSpeculativeDecodingS3DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelSpeculativeDecodingS3DataType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ModelSpeculativeDecodingS3DataType value: {data!r}"
        )
    return cast(ModelSpeculativeDecodingS3DataType, data)
