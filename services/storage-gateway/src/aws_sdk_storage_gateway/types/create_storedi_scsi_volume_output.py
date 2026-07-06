"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateStorediSCSIVolumeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.long
    import aws_sdk_storage_gateway.types.target_arn
    import aws_sdk_storage_gateway.types.volume_arn


class CreateStorediSCSIVolumeOutput(TypedDict, closed=True):
    volume_arn: NotRequired["aws_sdk_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The Amazon Resource Name (ARN) of the configured volume.</p>"""
    volume_size_in_bytes: "aws_sdk_storage_gateway.types.long.long"
    """<p>The size of the volume in bytes.</p>"""
    target_arn: NotRequired["aws_sdk_storage_gateway.types.target_arn.TargetARN"]
    """<p>The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name that initiators can use to connect to the target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStorediSCSIVolumeOutput) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["VolumeARN"] = value["volume_arn"]
    out["VolumeSizeInBytes"] = value.get("volume_size_in_bytes", 0)
    if "target_arn" in value:
        out["TargetARN"] = value["target_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStorediSCSIVolumeOutput:
    out: CreateStorediSCSIVolumeOutput = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    if "VolumeSizeInBytes" in data:
        out["volume_size_in_bytes"] = data["VolumeSizeInBytes"]
    else:
        out["volume_size_in_bytes"] = 0
    if "TargetARN" in data:
        out["target_arn"] = data["TargetARN"]
    return out
