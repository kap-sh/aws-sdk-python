"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileSystemOpenZFSOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.delete_file_system_open_zfs_option

DeleteFileSystemOpenZFSOptions: TypeAlias = list[
    "capo_fsx.types.delete_file_system_open_zfs_option.DeleteFileSystemOpenZFSOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileSystemOpenZFSOptions) -> list:
    import capo_fsx.types.delete_file_system_open_zfs_option

    out: list = []
    for item in value:
        out.append(
            capo_fsx.types.delete_file_system_open_zfs_option.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeleteFileSystemOpenZFSOptions:
    import capo_fsx.types.delete_file_system_open_zfs_option

    out: DeleteFileSystemOpenZFSOptions = []
    for item in data:
        out.append(
            capo_fsx.types.delete_file_system_open_zfs_option.deserialize_aws_json_1_1(
                item
            )
        )
    return out
