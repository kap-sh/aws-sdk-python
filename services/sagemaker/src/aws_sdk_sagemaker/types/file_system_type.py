"""Generated from Smithy shape ``com.amazonaws.sagemaker#FileSystemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FileSystemType: TypeAlias = Literal[
    "EFS",
    "FSxLustre",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EFS",
        "FSxLustre",
    )
)


def serialize_aws_json_1_1(value: FileSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileSystemType value: {data!r}")
    return cast(FileSystemType, data)
