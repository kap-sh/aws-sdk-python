"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_efs.types.file_system_description

FileSystemDescriptions: TypeAlias = list[
    "aws_sdk_efs.types.file_system_description.FileSystemDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemDescriptions) -> list:
    import aws_sdk_efs.types.file_system_description

    out: list = []
    for item in value:
        out.append(aws_sdk_efs.types.file_system_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> FileSystemDescriptions:
    import aws_sdk_efs.types.file_system_description

    out: FileSystemDescriptions = []
    for item in data:
        out.append(aws_sdk_efs.types.file_system_description.deserialize_json(item))
    return out
