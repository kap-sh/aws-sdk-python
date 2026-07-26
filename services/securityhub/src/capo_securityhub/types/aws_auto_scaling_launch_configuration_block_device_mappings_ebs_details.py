"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails(
    TypedDict, closed=True
):
    delete_on_termination: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to delete the volume when the instance is terminated.</p>"""
    encrypted: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to encrypt the volume.</p>"""
    iops: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of input/output (I/O) operations per second (IOPS) to provision for the volume.</p> <p>Only supported for <code>gp3</code> or <code>io1</code> volumes. Required for <code>io1</code> volumes. Not used with <code>standard</code>, <code>gp2</code>, <code>st1</code>, or <code>sc1</code> volumes.</p>"""
    snapshot_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The snapshot ID of the volume to use.</p> <p>You must specify either <code>VolumeSize</code> or <code>SnapshotId</code>.</p>"""
    volume_size: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The volume size, in GiBs. The following are the supported volumes sizes for each volume type:</p> <ul> <li> <p>gp2 and gp3: 1-16,384</p> </li> <li> <p>io1: 4-16,384</p> </li> <li> <p>st1 and sc1: 125-16,384</p> </li> <li> <p>standard: 1-1,024</p> </li> </ul> <p>You must specify either <code>SnapshotId</code> or <code>VolumeSize</code>. If you specify both <code>SnapshotId</code> and <code>VolumeSize</code>, the volume size must be equal or greater than the size of the snapshot.</p>"""
    volume_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The volume type. Valid values are as follows:</p> <ul> <li> <p> <code>gp2</code> </p> </li> <li> <p> <code>gp3</code> </p> </li> <li> <p> <code>io1</code> </p> </li> <li> <p> <code>sc1</code> </p> </li> <li> <p> <code>st1</code> </p> </li> <li> <p> <code>standard</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails,
) -> dict:
    out: dict = {}
    if "delete_on_termination" in value:
        out["DeleteOnTermination"] = value["delete_on_termination"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "volume_size" in value:
        out["VolumeSize"] = value["volume_size"]
    if "volume_type" in value:
        out["VolumeType"] = value["volume_type"]
    return out


def deserialize_json(
    data: dict,
) -> AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails:
    out: AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails = {}  # type: ignore[typeddict-item]
    if "DeleteOnTermination" in data:
        out["delete_on_termination"] = data["DeleteOnTermination"]
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    if "VolumeSize" in data:
        out["volume_size"] = data["VolumeSize"]
    if "VolumeType" in data:
        out["volume_type"] = data["VolumeType"]
    return out
