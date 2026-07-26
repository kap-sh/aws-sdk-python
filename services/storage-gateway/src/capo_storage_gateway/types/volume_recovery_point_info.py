"""Generated from Smithy shape ``com.amazonaws.storagegateway#VolumeRecoveryPointInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.long
    import capo_storage_gateway.types.string
    import capo_storage_gateway.types.volume_arn


class VolumeRecoveryPointInfo(TypedDict, closed=True):
    volume_arn: NotRequired["capo_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The Amazon Resource Name (ARN) of the volume target.</p>"""
    volume_size_in_bytes: "capo_storage_gateway.types.long.long"
    """<p>The size of the volume in bytes.</p>"""
    volume_usage_in_bytes: "capo_storage_gateway.types.long.long"
    """<p>The size of the data stored on the volume in bytes.</p> <note> <p>This value is not available for volumes created prior to May 13, 2015, until you store data on the volume.</p> </note>"""
    volume_recovery_point_time: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>The time the recovery point was taken.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeRecoveryPointInfo) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["VolumeARN"] = value["volume_arn"]
    out["VolumeSizeInBytes"] = value.get("volume_size_in_bytes", 0)
    out["VolumeUsageInBytes"] = value.get("volume_usage_in_bytes", 0)
    if "volume_recovery_point_time" in value:
        out["VolumeRecoveryPointTime"] = value["volume_recovery_point_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VolumeRecoveryPointInfo:
    out: VolumeRecoveryPointInfo = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    if "VolumeSizeInBytes" in data:
        out["volume_size_in_bytes"] = data["VolumeSizeInBytes"]
    else:
        out["volume_size_in_bytes"] = 0
    if "VolumeUsageInBytes" in data:
        out["volume_usage_in_bytes"] = data["VolumeUsageInBytes"]
    else:
        out["volume_usage_in_bytes"] = 0
    if "VolumeRecoveryPointTime" in data:
        out["volume_recovery_point_time"] = data["VolumeRecoveryPointTime"]
    return out
