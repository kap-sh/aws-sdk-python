"""Generated from Smithy shape ``com.amazonaws.ec2#EbsBlockDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.kms_key_id
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.volume_type


class EbsBlockDeviceResponse(TypedDict, closed=True):
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is encrypted.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is deleted on instance termination.</p>"""
    iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS). For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.</p>"""
    throughput: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.kms_key_id.KmsKeyId"]
    """<p>Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiBs.</p>"""
    volume_type: NotRequired["aws_sdk_ec2.types.volume_type.VolumeType"]
    r"""<p>The volume type. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html\">Amazon EBS volume types</a> in the <i>Amazon EBS User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EbsBlockDeviceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "encrypted" in value:
        pairs.append((f"{prefix}.Encrypted", "true" if value["encrypted"] else "false"))
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{prefix}.DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "iops" in value:
        pairs.append((f"{prefix}.Iops", str(value["iops"])))
    if "throughput" in value:
        pairs.append((f"{prefix}.Throughput", str(value["throughput"])))
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "volume_size" in value:
        pairs.append((f"{prefix}.VolumeSize", str(value["volume_size"])))
    if "volume_type" in value:
        import aws_sdk_ec2.types.volume_type

        aws_sdk_ec2.types.volume_type.serialize_ec2_query(
            value["volume_type"], pairs, f"{prefix}.VolumeType"
        )


def deserialize_ec2_query(el: Element) -> EbsBlockDeviceResponse:
    out: EbsBlockDeviceResponse = {}  # type: ignore[typeddict-item]
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_throughput = el.find("Throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_volume_size = el.find("VolumeSize")
    if child_volume_size is not None:
        out["volume_size"] = int(child_volume_size.text or "")
    child_volume_type = el.find("VolumeType")
    if child_volume_type is not None:
        import aws_sdk_ec2.types.volume_type

        out["volume_type"] = aws_sdk_ec2.types.volume_type.deserialize_ec2_query(
            child_volume_type
        )
    return out
