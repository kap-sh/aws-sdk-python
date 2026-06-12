"""Generated from Smithy shape ``com.amazonaws.sagemaker#FileSystemAccessMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FileSystemAccessMode: TypeAlias = Literal[
    "rw",
    "ro",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "rw",
        "ro",
    )
)


def serialize_aws_json_1_1(value: FileSystemAccessMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemAccessMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileSystemAccessMode value: {data!r}")
    return cast(FileSystemAccessMode, data)
