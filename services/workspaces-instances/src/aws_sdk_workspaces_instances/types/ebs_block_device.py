"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EbsBlockDevice``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.kms_key_id
    import aws_sdk_workspaces_instances.types.non_negative_integer
    import aws_sdk_workspaces_instances.types.volume_type_enum

class EbsBlockDevice(TypedDict):
    volume_type: NotRequired["aws_sdk_workspaces_instances.types.volume_type_enum.VolumeTypeEnum"]
    """<p>Type of EBS volume (e.g., gp2, io1).</p>"""
    encrypted: NotRequired["bool"]
    """<p>Indicates if the volume is encrypted.</p>"""
    kms_key_id: NotRequired["aws_sdk_workspaces_instances.types.kms_key_id.KmsKeyId"]
    """<p>KMS key used for volume encryption.</p>"""
    iops: NotRequired["aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"]
    """<p>Input/output operations per second for the volume.</p>"""
    throughput: NotRequired["aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"]
    """<p>Volume data transfer rate.</p>"""
    volume_size: NotRequired["aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"]
    """<p>Size of the EBS volume in gigabytes.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EbsBlockDevice) -> dict:
    out: dict = {}
    if "volume_type" in value:
        import aws_sdk_workspaces_instances.types.volume_type_enum
        out["VolumeType"] = aws_sdk_workspaces_instances.types.volume_type_enum.serialize_aws_json_1_0(value["volume_type"])
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "throughput" in value:
        out["Throughput"] = value["throughput"]
    if "volume_size" in value:
        out["VolumeSize"] = value["volume_size"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EbsBlockDevice:
    out: EbsBlockDevice = {}  # type: ignore[typeddict-item]
    if "VolumeType" in data:
        import aws_sdk_workspaces_instances.types.volume_type_enum
        out["volume_type"] = aws_sdk_workspaces_instances.types.volume_type_enum.deserialize_aws_json_1_0(data["VolumeType"])
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "Throughput" in data:
        out["throughput"] = data["Throughput"]
    if "VolumeSize" in data:
        out["volume_size"] = data["VolumeSize"]
    return out