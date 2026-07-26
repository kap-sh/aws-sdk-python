"""Generated from Smithy shape ``com.amazonaws.ecs#VolumeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.volume

VolumeList: TypeAlias = list["capo_ecs.types.volume.Volume"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeList) -> list:
    import capo_ecs.types.volume

    out: list = []
    for item in value:
        out.append(capo_ecs.types.volume.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> VolumeList:
    import capo_ecs.types.volume

    out: VolumeList = []
    for item in data:
        out.append(capo_ecs.types.volume.deserialize_aws_json_1_1(item))
    return out
