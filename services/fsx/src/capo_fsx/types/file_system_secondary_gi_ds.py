"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemSecondaryGIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.file_system_gid

FileSystemSecondaryGIDs: TypeAlias = list[
    "capo_fsx.types.file_system_gid.FileSystemGID"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemSecondaryGIDs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FileSystemSecondaryGIDs:
    return list(data)
