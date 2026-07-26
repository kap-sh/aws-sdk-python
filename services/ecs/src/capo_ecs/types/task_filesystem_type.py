"""Generated from Smithy shape ``com.amazonaws.ecs#TaskFilesystemType``."""

from typing import Literal, TypeAlias, cast

TaskFilesystemType: TypeAlias = Literal[
    "ext3",
    "ext4",
    "xfs",
    "ntfs",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskFilesystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskFilesystemType:
    return cast(TaskFilesystemType, data)
