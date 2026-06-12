"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteOpenZFSVolumeOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.delete_open_zfs_volume_option

DeleteOpenZFSVolumeOptions: TypeAlias = list[
    "aws_sdk_fsx.types.delete_open_zfs_volume_option.DeleteOpenZFSVolumeOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOpenZFSVolumeOptions) -> list:
    import aws_sdk_fsx.types.delete_open_zfs_volume_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fsx.types.delete_open_zfs_volume_option.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeleteOpenZFSVolumeOptions:
    import aws_sdk_fsx.types.delete_open_zfs_volume_option

    out: DeleteOpenZFSVolumeOptions = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.delete_open_zfs_volume_option.deserialize_aws_json_1_1(
                item
            )
        )
    return out
