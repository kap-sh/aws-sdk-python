"""Generated from Smithy shape ``com.amazonaws.sagemaker#FileSystemAccessMode``."""

from typing import Literal, TypeAlias, cast

FileSystemAccessMode: TypeAlias = Literal[
    "rw",
    "ro",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemAccessMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemAccessMode:
    return cast(FileSystemAccessMode, data)
