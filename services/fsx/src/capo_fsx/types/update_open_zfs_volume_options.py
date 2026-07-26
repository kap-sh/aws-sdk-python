"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateOpenZFSVolumeOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.update_open_zfs_volume_option

UpdateOpenZFSVolumeOptions: TypeAlias = list[
    "capo_fsx.types.update_open_zfs_volume_option.UpdateOpenZFSVolumeOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOpenZFSVolumeOptions) -> list:
    import capo_fsx.types.update_open_zfs_volume_option

    out: list = []
    for item in value:
        out.append(
            capo_fsx.types.update_open_zfs_volume_option.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateOpenZFSVolumeOptions:
    import capo_fsx.types.update_open_zfs_volume_option

    out: UpdateOpenZFSVolumeOptions = []
    for item in data:
        out.append(
            capo_fsx.types.update_open_zfs_volume_option.deserialize_aws_json_1_1(item)
        )
    return out
