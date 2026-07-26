"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateSnapshotOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.snapshot_id
    import capo_storage_gateway.types.volume_arn


class CreateSnapshotOutput(TypedDict, closed=True):
    volume_arn: NotRequired["capo_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The Amazon Resource Name (ARN) of the volume of which the snapshot was taken.</p>"""
    snapshot_id: NotRequired["capo_storage_gateway.types.snapshot_id.SnapshotId"]
    """<p>The snapshot ID that is used to refer to the snapshot in future operations such as describing snapshots (Amazon Elastic Compute Cloud API <code>DescribeSnapshots</code>) or creating a volume from a snapshot (<a>CreateStorediSCSIVolume</a>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotOutput) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["VolumeARN"] = value["volume_arn"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotOutput:
    out: CreateSnapshotOutput = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    return out
