"""Generated from Smithy shape ``com.amazonaws.ecs#VolumeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.volume

VolumeList: TypeAlias = list["aws_sdk_ecs.types.volume.Volume"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeList) -> list:
    import aws_sdk_ecs.types.volume

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.volume.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> VolumeList:
    import aws_sdk_ecs.types.volume

    out: VolumeList = []
    for item in data:
        out.append(aws_sdk_ecs.types.volume.deserialize_aws_json_1_1(item))
    return out
