"""Generated from Smithy shape ``com.amazonaws.guardduty#VolumeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.string


class VolumeDetail(TypedDict, closed=True):
    volume_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>EBS volume ARN information.</p>"""
    volume_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The EBS volume type.</p>"""
    device_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The device name for the EBS volume.</p>"""
    volume_size_in_gb: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>EBS volume size in GB.</p>"""
    encryption_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>EBS volume encryption type.</p>"""
    snapshot_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Snapshot ARN of the EBS volume.</p>"""
    kms_key_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>KMS key ARN used to encrypt the EBS volume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VolumeDetail) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["volumeArn"] = value["volume_arn"]
    if "volume_type" in value:
        out["volumeType"] = value["volume_type"]
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    if "volume_size_in_gb" in value:
        out["volumeSizeInGB"] = value["volume_size_in_gb"]
    if "encryption_type" in value:
        out["encryptionType"] = value["encryption_type"]
    if "snapshot_arn" in value:
        out["snapshotArn"] = value["snapshot_arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> VolumeDetail:
    out: VolumeDetail = {}  # type: ignore[typeddict-item]
    if "volumeArn" in data:
        out["volume_arn"] = data["volumeArn"]
    if "volumeType" in data:
        out["volume_type"] = data["volumeType"]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    if "volumeSizeInGB" in data:
        out["volume_size_in_gb"] = data["volumeSizeInGB"]
    if "encryptionType" in data:
        out["encryption_type"] = data["encryptionType"]
    if "snapshotArn" in data:
        out["snapshot_arn"] = data["snapshotArn"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
