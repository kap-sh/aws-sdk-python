"""Generated from Smithy shape ``com.amazonaws.s3files#FileSystems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3files.types.list_file_systems_description

FileSystems: TypeAlias = list[
    "capo_s3files.types.list_file_systems_description.ListFileSystemsDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSystems) -> list:
    import capo_s3files.types.list_file_systems_description

    out: list = []
    for item in value:
        out.append(
            capo_s3files.types.list_file_systems_description.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FileSystems:
    import capo_s3files.types.list_file_systems_description

    out: FileSystems = []
    for item in data:
        out.append(
            capo_s3files.types.list_file_systems_description.deserialize_json(item)
        )
    return out
