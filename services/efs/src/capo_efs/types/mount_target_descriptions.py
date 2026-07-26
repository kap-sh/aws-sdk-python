"""Generated from Smithy shape ``com.amazonaws.efs#MountTargetDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_efs.types.mount_target_description

MountTargetDescriptions: TypeAlias = list[
    "capo_efs.types.mount_target_description.MountTargetDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: MountTargetDescriptions) -> list:
    import capo_efs.types.mount_target_description

    out: list = []
    for item in value:
        out.append(capo_efs.types.mount_target_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> MountTargetDescriptions:
    import capo_efs.types.mount_target_description

    out: MountTargetDescriptions = []
    for item in data:
        out.append(capo_efs.types.mount_target_description.deserialize_json(item))
    return out
