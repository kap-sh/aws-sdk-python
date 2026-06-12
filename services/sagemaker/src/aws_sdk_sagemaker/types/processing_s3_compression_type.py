"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3CompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProcessingS3CompressionType: TypeAlias = Literal[
    "None",
    "Gzip",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "Gzip",
    )
)


def serialize_aws_json_1_1(value: ProcessingS3CompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3CompressionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProcessingS3CompressionType value: {data!r}"
        )
    return cast(ProcessingS3CompressionType, data)
