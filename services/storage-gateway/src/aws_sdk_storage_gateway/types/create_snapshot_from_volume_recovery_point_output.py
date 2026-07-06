"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateSnapshotFromVolumeRecoveryPointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.snapshot_id
    import aws_sdk_storage_gateway.types.string
    import aws_sdk_storage_gateway.types.volume_arn


class CreateSnapshotFromVolumeRecoveryPointOutput(TypedDict, closed=True):
    snapshot_id: NotRequired["aws_sdk_storage_gateway.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_arn: NotRequired["aws_sdk_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return to retrieve the TargetARN for specified VolumeARN.</p>"""
    volume_recovery_point_time: NotRequired[
        "aws_sdk_storage_gateway.types.string.string"
    ]
    """<p>The time the volume was created from the recovery point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotFromVolumeRecoveryPointOutput) -> dict:
    out: dict = {}
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "volume_arn" in value:
        out["VolumeARN"] = value["volume_arn"]
    if "volume_recovery_point_time" in value:
        out["VolumeRecoveryPointTime"] = value["volume_recovery_point_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotFromVolumeRecoveryPointOutput:
    out: CreateSnapshotFromVolumeRecoveryPointOutput = {}  # type: ignore[typeddict-item]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    if "VolumeRecoveryPointTime" in data:
        out["volume_recovery_point_time"] = data["VolumeRecoveryPointTime"]
    return out
