"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonVolumeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_volume

DaemonVolumeList: TypeAlias = list["capo_ecs.types.daemon_volume.DaemonVolume"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonVolumeList) -> list:
    import capo_ecs.types.daemon_volume

    out: list = []
    for item in value:
        out.append(capo_ecs.types.daemon_volume.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonVolumeList:
    import capo_ecs.types.daemon_volume

    out: DaemonVolumeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.daemon_volume.deserialize_aws_json_1_1(item))
    return out
