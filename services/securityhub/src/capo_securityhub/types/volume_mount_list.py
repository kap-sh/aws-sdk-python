"""Generated from Smithy shape ``com.amazonaws.securityhub#VolumeMountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.volume_mount

VolumeMountList: TypeAlias = list["capo_securityhub.types.volume_mount.VolumeMount"]


# --- restJson1 ser/de ---
def serialize_json(value: VolumeMountList) -> list:
    import capo_securityhub.types.volume_mount

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.volume_mount.serialize_json(item))
    return out


def deserialize_json(data: list) -> VolumeMountList:
    import capo_securityhub.types.volume_mount

    out: VolumeMountList = []
    for item in data:
        out.append(capo_securityhub.types.volume_mount.deserialize_json(item))
    return out
