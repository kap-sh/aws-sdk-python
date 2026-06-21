"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FileType``."""

from typing import Literal, TypeAlias, cast

FileType: TypeAlias = Literal[
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/pdf",
    "image/png",
    "image/jpeg",
    "image/svg+xml",
    "text/csv",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FileType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FileType:
    return cast(FileType, data)
