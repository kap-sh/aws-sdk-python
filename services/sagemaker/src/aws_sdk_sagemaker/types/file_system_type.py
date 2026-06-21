"""Generated from Smithy shape ``com.amazonaws.sagemaker#FileSystemType``."""

from typing import Literal, TypeAlias, cast

FileSystemType: TypeAlias = Literal[
    "EFS",
    "FSxLustre",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemType:
    return cast(FileSystemType, data)
