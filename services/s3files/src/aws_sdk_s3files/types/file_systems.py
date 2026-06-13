"""Generated from Smithy shape ``com.amazonaws.s3files#FileSystems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3files.types.list_file_systems_description

FileSystems: TypeAlias = list[
    "aws_sdk_s3files.types.list_file_systems_description.ListFileSystemsDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSystems) -> list:
    import aws_sdk_s3files.types.list_file_systems_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_s3files.types.list_file_systems_description.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FileSystems:
    import aws_sdk_s3files.types.list_file_systems_description

    out: FileSystems = []
    for item in data:
        out.append(
            aws_sdk_s3files.types.list_file_systems_description.deserialize_json(item)
        )
    return out
