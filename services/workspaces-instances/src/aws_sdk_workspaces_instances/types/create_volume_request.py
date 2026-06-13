"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CreateVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.client_token
    import aws_sdk_workspaces_instances.types.kms_key_id
    import aws_sdk_workspaces_instances.types.non_negative_integer
    import aws_sdk_workspaces_instances.types.snapshot_id
    import aws_sdk_workspaces_instances.types.string64
    import aws_sdk_workspaces_instances.types.tag_specifications
    import aws_sdk_workspaces_instances.types.volume_type_enum


class CreateVolumeRequest(TypedDict):
    availability_zone: "aws_sdk_workspaces_instances.types.string64.String64"
    """<p>Availability zone for the volume.</p>"""
    client_token: NotRequired[
        "aws_sdk_workspaces_instances.types.client_token.ClientToken"
    ]
    """<p>Unique token to prevent duplicate volume creation.</p>"""
    encrypted: NotRequired["bool"]
    """<p>Indicates if the volume should be encrypted.</p>"""
    iops: NotRequired[
        "aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Input/output operations per second for the volume.</p>"""
    kms_key_id: NotRequired["aws_sdk_workspaces_instances.types.kms_key_id.KmsKeyId"]
    """<p>KMS key for volume encryption.</p>"""
    size_in_gb: NotRequired[
        "aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Volume size in gigabytes.</p>"""
    snapshot_id: NotRequired[
        "aws_sdk_workspaces_instances.types.snapshot_id.SnapshotId"
    ]
    """<p>Source snapshot for volume creation.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_workspaces_instances.types.tag_specifications.TagSpecifications"
    ]
    """<p>Metadata tags for the volume.</p>"""
    throughput: NotRequired[
        "aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Volume throughput performance.</p>"""
    volume_type: NotRequired[
        "aws_sdk_workspaces_instances.types.volume_type_enum.VolumeTypeEnum"
    ]
    """<p>Type of EBS volume.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVolumeRequest) -> dict:
    out: dict = {}
    out["AvailabilityZone"] = value["availability_zone"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "size_in_gb" in value:
        out["SizeInGB"] = value["size_in_gb"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "tag_specifications" in value:
        import aws_sdk_workspaces_instances.types.tag_specifications

        out["TagSpecifications"] = (
            aws_sdk_workspaces_instances.types.tag_specifications.serialize_aws_json_1_0(
                value["tag_specifications"]
            )
        )
    if "throughput" in value:
        out["Throughput"] = value["throughput"]
    if "volume_type" in value:
        import aws_sdk_workspaces_instances.types.volume_type_enum

        out["VolumeType"] = (
            aws_sdk_workspaces_instances.types.volume_type_enum.serialize_aws_json_1_0(
                value["volume_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVolumeRequest:
    out: CreateVolumeRequest = {}  # type: ignore[typeddict-item]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    else:
        raise DeserializationError("CreateVolumeRequest.availability_zone required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "SizeInGB" in data:
        out["size_in_gb"] = data["SizeInGB"]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    if "TagSpecifications" in data:
        import aws_sdk_workspaces_instances.types.tag_specifications

        out["tag_specifications"] = (
            aws_sdk_workspaces_instances.types.tag_specifications.deserialize_aws_json_1_0(
                data["TagSpecifications"]
            )
        )
    if "Throughput" in data:
        out["throughput"] = data["Throughput"]
    if "VolumeType" in data:
        import aws_sdk_workspaces_instances.types.volume_type_enum

        out["volume_type"] = (
            aws_sdk_workspaces_instances.types.volume_type_enum.deserialize_aws_json_1_0(
                data["VolumeType"]
            )
        )
    return out
