"""Generated from Smithy shape ``com.amazonaws.storagegateway#VolumeARNs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.volume_arn

VolumeARNs: TypeAlias = list["aws_sdk_storage_gateway.types.volume_arn.VolumeARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeARNs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VolumeARNs:
    return list(data)
