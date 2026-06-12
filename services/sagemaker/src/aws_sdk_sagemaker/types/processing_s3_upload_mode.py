"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3UploadMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProcessingS3UploadMode: TypeAlias = Literal[
    "Continuous",
    "EndOfJob",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Continuous",
        "EndOfJob",
    )
)


def serialize_aws_json_1_1(value: ProcessingS3UploadMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3UploadMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProcessingS3UploadMode value: {data!r}")
    return cast(ProcessingS3UploadMode, data)
