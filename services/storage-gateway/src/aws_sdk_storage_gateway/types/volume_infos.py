"""Generated from Smithy shape ``com.amazonaws.storagegateway#VolumeInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.volume_info

VolumeInfos: TypeAlias = list["aws_sdk_storage_gateway.types.volume_info.VolumeInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeInfos) -> list:
    import aws_sdk_storage_gateway.types.volume_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.volume_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VolumeInfos:
    import aws_sdk_storage_gateway.types.volume_info

    out: VolumeInfos = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.volume_info.deserialize_aws_json_1_1(item)
        )
    return out
