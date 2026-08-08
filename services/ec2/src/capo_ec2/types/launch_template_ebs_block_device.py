"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateEbsBlockDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.kms_key_id
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.volume_type


class LaunchTemplateEbsBlockDevice(TypedDict, closed=True):
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the EBS volume is encrypted.</p>"""
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the EBS volume is deleted on instance termination.</p>"""
    iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) that the volume supports. </p>"""
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p>"""
    volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The volume type.</p>"""
    throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p>"""
    volume_initialization_rate: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) specified for the volume, in MiB/s. If no volume initialization rate was specified, the value is <code>null</code>.</p>"""
    ebs_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateEbsBlockDevice, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "volume_size" in value:
        pairs.append((f"{key_prefix}VolumeSize", str(value["volume_size"])))
    if "volume_type" in value:
        import capo_ec2.types.volume_type

        capo_ec2.types.volume_type.serialize_ec2_query(
            value["volume_type"], pairs, f"{key_prefix}VolumeType"
        )
    if "throughput" in value:
        pairs.append((f"{key_prefix}Throughput", str(value["throughput"])))
    if "volume_initialization_rate" in value:
        pairs.append(
            (
                f"{key_prefix}VolumeInitializationRate",
                str(value["volume_initialization_rate"]),
            )
        )
    if "ebs_card_index" in value:
        pairs.append((f"{key_prefix}EbsCardIndex", str(value["ebs_card_index"])))


def deserialize_ec2_query(el: Element) -> LaunchTemplateEbsBlockDevice:
    out: LaunchTemplateEbsBlockDevice = {}  # type: ignore[typeddict-item]
    child_encrypted = el.find("encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_delete_on_termination = el.find("deleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_iops = el.find("iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_kms_key_id = el.find("kmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_volume_size = el.find("volumeSize")
    if child_volume_size is not None:
        out["volume_size"] = int(child_volume_size.text or "")
    child_volume_type = el.find("volumeType")
    if child_volume_type is not None:
        import capo_ec2.types.volume_type

        out["volume_type"] = capo_ec2.types.volume_type.deserialize_ec2_query(
            child_volume_type
        )
    child_throughput = el.find("throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
    child_volume_initialization_rate = el.find("volumeInitializationRate")
    if child_volume_initialization_rate is not None:
        out["volume_initialization_rate"] = int(
            child_volume_initialization_rate.text or ""
        )
    child_ebs_card_index = el.find("ebsCardIndex")
    if child_ebs_card_index is not None:
        out["ebs_card_index"] = int(child_ebs_card_index.text or "")
    return out
