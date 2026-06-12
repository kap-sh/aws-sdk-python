"""Generated from Smithy shape ``com.amazonaws.imagebuilder#EbsInstanceBlockDeviceSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.ebs_iops_integer
    import aws_sdk_imagebuilder.types.ebs_volume_size_integer
    import aws_sdk_imagebuilder.types.ebs_volume_throughput
    import aws_sdk_imagebuilder.types.ebs_volume_type
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.nullable_boolean


class EbsInstanceBlockDeviceSpecification(TypedDict):
    encrypted: NotRequired[
        "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Use to configure device encryption.</p>"""
    delete_on_termination: NotRequired[
        "aws_sdk_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Use to configure delete on termination of the associated device.</p>"""
    iops: NotRequired["aws_sdk_imagebuilder.types.ebs_iops_integer.EbsIopsInteger"]
    """<p>Use to configure device IOPS.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key to use when encrypting the device. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    snapshot_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The snapshot that defines the device contents.</p>"""
    volume_size: NotRequired[
        "aws_sdk_imagebuilder.types.ebs_volume_size_integer.EbsVolumeSizeInteger"
    ]
    """<p>Use to override the device's volume size.</p>"""
    volume_type: NotRequired["aws_sdk_imagebuilder.types.ebs_volume_type.EbsVolumeType"]
    """<p>Use to override the device's volume type.</p>"""
    throughput: NotRequired[
        "aws_sdk_imagebuilder.types.ebs_volume_throughput.EbsVolumeThroughput"
    ]
    """<p> <b>For GP3 volumes only</b> – The throughput in MiB/s that the volume supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsInstanceBlockDeviceSpecification) -> dict:
    out: dict = {}
    if "encrypted" in value:
        out["encrypted"] = value["encrypted"]
    if "delete_on_termination" in value:
        out["deleteOnTermination"] = value["delete_on_termination"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "snapshot_id" in value:
        out["snapshotId"] = value["snapshot_id"]
    if "volume_size" in value:
        out["volumeSize"] = value["volume_size"]
    if "volume_type" in value:
        import aws_sdk_imagebuilder.types.ebs_volume_type

        out["volumeType"] = aws_sdk_imagebuilder.types.ebs_volume_type.serialize_json(
            value["volume_type"]
        )
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    return out


def deserialize_json(data: dict) -> EbsInstanceBlockDeviceSpecification:
    out: EbsInstanceBlockDeviceSpecification = {}  # type: ignore[typeddict-item]
    if "encrypted" in data:
        out["encrypted"] = data["encrypted"]
    if "deleteOnTermination" in data:
        out["delete_on_termination"] = data["deleteOnTermination"]
    if "iops" in data:
        out["iops"] = data["iops"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "snapshotId" in data:
        out["snapshot_id"] = data["snapshotId"]
    if "volumeSize" in data:
        out["volume_size"] = data["volumeSize"]
    if "volumeType" in data:
        import aws_sdk_imagebuilder.types.ebs_volume_type

        out["volume_type"] = (
            aws_sdk_imagebuilder.types.ebs_volume_type.deserialize_json(
                data["volumeType"]
            )
        )
    if "throughput" in data:
        out["throughput"] = data["throughput"]
    return out
