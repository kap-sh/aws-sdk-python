"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails(TypedDict, closed=True):
    delete_on_termination: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether the EBS volume is deleted on instance termination. </p>"""
    encrypted: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. If you're creating a volume from a snapshot, you can't specify an encryption value. </p>"""
    iops: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The number of I/O operations per second (IOPS). </p>"""
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the symmetric Key Management Service (KMS) customer managed key used for encryption. </p>"""
    snapshot_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the EBS snapshot. </p>"""
    throughput: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The throughput to provision for a gp3 volume, with a maximum of 1,000 MiB/s. </p>"""
    volume_size: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. </p>"""
    volume_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The volume type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails,
) -> dict:
    out: dict = {}
    if "delete_on_termination" in value:
        out["DeleteOnTermination"] = value["delete_on_termination"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "throughput" in value:
        out["Throughput"] = value["throughput"]
    if "volume_size" in value:
        out["VolumeSize"] = value["volume_size"]
    if "volume_type" in value:
        out["VolumeType"] = value["volume_type"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails:
    out: AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails = {}  # type: ignore[typeddict-item]
    if "DeleteOnTermination" in data:
        out["delete_on_termination"] = data["DeleteOnTermination"]
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    if "Throughput" in data:
        out["throughput"] = data["Throughput"]
    if "VolumeSize" in data:
        out["volume_size"] = data["VolumeSize"]
    if "VolumeType" in data:
        out["volume_type"] = data["VolumeType"]
    return out
