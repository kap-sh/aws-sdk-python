"""Generated from Smithy shape ``com.amazonaws.s3files#MountTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3files.types.list_mount_targets_description

MountTargets: TypeAlias = list[
    "aws_sdk_s3files.types.list_mount_targets_description.ListMountTargetsDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: MountTargets) -> list:
    import aws_sdk_s3files.types.list_mount_targets_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_s3files.types.list_mount_targets_description.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MountTargets:
    import aws_sdk_s3files.types.list_mount_targets_description

    out: MountTargets = []
    for item in data:
        out.append(
            aws_sdk_s3files.types.list_mount_targets_description.deserialize_json(item)
        )
    return out
