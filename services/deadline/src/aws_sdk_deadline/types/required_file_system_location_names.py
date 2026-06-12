"""Generated from Smithy shape ``com.amazonaws.deadline#RequiredFileSystemLocationNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.file_system_location_name

RequiredFileSystemLocationNames: TypeAlias = list[
    "aws_sdk_deadline.types.file_system_location_name.FileSystemLocationName"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredFileSystemLocationNames) -> list:
    return list(value)


def deserialize_json(data: list) -> RequiredFileSystemLocationNames:
    return list(data)
