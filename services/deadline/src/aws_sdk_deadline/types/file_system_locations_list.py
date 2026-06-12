"""Generated from Smithy shape ``com.amazonaws.deadline#FileSystemLocationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.file_system_location

FileSystemLocationsList: TypeAlias = list[
    "aws_sdk_deadline.types.file_system_location.FileSystemLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemLocationsList) -> list:
    import aws_sdk_deadline.types.file_system_location

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.file_system_location.serialize_json(item))
    return out


def deserialize_json(data: list) -> FileSystemLocationsList:
    import aws_sdk_deadline.types.file_system_location

    out: FileSystemLocationsList = []
    for item in data:
        out.append(aws_sdk_deadline.types.file_system_location.deserialize_json(item))
    return out
