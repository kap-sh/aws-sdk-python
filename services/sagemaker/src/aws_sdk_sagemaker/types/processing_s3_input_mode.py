"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3InputMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProcessingS3InputMode: TypeAlias = Literal[
    "Pipe",
    "File",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pipe",
        "File",
    )
)


def serialize_aws_json_1_1(value: ProcessingS3InputMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingS3InputMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProcessingS3InputMode value: {data!r}")
    return cast(ProcessingS3InputMode, data)
