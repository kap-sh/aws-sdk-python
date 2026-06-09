"""Generated from Smithy shape ``com.amazonaws.ecs#TaskFilesystemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

TaskFilesystemType: TypeAlias = Literal[
    "ext3",
    "ext4",
    "xfs",
    "ntfs",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ext3",
        "ext4",
        "xfs",
        "ntfs",
    )
)


def serialize_aws_json_1_1(value: TaskFilesystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskFilesystemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskFilesystemType value: {data!r}")
    return cast(TaskFilesystemType, data)
