"""Generated from Smithy shape ``com.amazonaws.securityhub#VolumeMountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.volume_mount

VolumeMountList: TypeAlias = list["aws_sdk_securityhub.types.volume_mount.VolumeMount"]


# --- restJson1 ser/de ---
def serialize_json(value: VolumeMountList) -> list:
    import aws_sdk_securityhub.types.volume_mount

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.volume_mount.serialize_json(item))
    return out


def deserialize_json(data: list) -> VolumeMountList:
    import aws_sdk_securityhub.types.volume_mount

    out: VolumeMountList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.volume_mount.deserialize_json(item))
    return out
