"""Generated from Smithy shape ``com.amazonaws.ecs#VolumeFromList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.volume_from

VolumeFromList: TypeAlias = list["capo_ecs.types.volume_from.VolumeFrom"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeFromList) -> list:
    import capo_ecs.types.volume_from

    out: list = []
    for item in value:
        out.append(capo_ecs.types.volume_from.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> VolumeFromList:
    import capo_ecs.types.volume_from

    out: VolumeFromList = []
    for item in data:
        out.append(capo_ecs.types.volume_from.deserialize_aws_json_1_1(item))
    return out
