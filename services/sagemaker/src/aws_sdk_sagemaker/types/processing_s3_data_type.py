"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3DataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProcessingS3DataType: TypeAlias = Literal[
    "ManifestFile",
    "S3Prefix",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ManifestFile",
        "S3Prefix",
    )
)


def serialize_aws_json_1_1(value: ProcessingS3DataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3DataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProcessingS3DataType value: {data!r}")
    return cast(ProcessingS3DataType, data)
