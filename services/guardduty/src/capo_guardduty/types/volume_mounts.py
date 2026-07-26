"""Generated from Smithy shape ``com.amazonaws.guardduty#VolumeMounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.volume_mount

VolumeMounts: TypeAlias = list["capo_guardduty.types.volume_mount.VolumeMount"]


# --- restJson1 ser/de ---
def serialize_json(value: VolumeMounts) -> list:
    import capo_guardduty.types.volume_mount

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.volume_mount.serialize_json(item))
    return out


def deserialize_json(data: list) -> VolumeMounts:
    import capo_guardduty.types.volume_mount

    out: VolumeMounts = []
    for item in data:
        out.append(capo_guardduty.types.volume_mount.deserialize_json(item))
    return out
