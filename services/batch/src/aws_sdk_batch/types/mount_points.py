"""Generated from Smithy shape ``com.amazonaws.batch#MountPoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.mount_point

MountPoints: TypeAlias = list["aws_sdk_batch.types.mount_point.MountPoint"]


# --- restJson1 ser/de ---
def serialize_json(value: MountPoints) -> list:
    import aws_sdk_batch.types.mount_point

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.mount_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> MountPoints:
    import aws_sdk_batch.types.mount_point

    out: MountPoints = []
    for item in data:
        out.append(aws_sdk_batch.types.mount_point.deserialize_json(item))
    return out
