"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesEbs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.string


class ScheduledInstancesEbs(TypedDict, closed=True):
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is deleted on instance termination.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is encrypted. You can attached encrypted volumes only to instances that support them.</p>"""
    iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) to provision for a <code>gp3</code>, <code>io1</code>, or <code>io2</code> volume.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p> <p>Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size.</p>"""
    volume_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The volume type.</p> <p>Default: <code>gp2</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesEbs, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{prefix}.DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "encrypted" in value:
        pairs.append((f"{prefix}.Encrypted", "true" if value["encrypted"] else "false"))
    if "iops" in value:
        pairs.append((f"{prefix}.Iops", str(value["iops"])))
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "volume_size" in value:
        pairs.append((f"{prefix}.VolumeSize", str(value["volume_size"])))
    if "volume_type" in value:
        pairs.append((f"{prefix}.VolumeType", str(value["volume_type"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesEbs:
    out: ScheduledInstancesEbs = {}  # type: ignore[typeddict-item]
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_volume_size = el.find("VolumeSize")
    if child_volume_size is not None:
        out["volume_size"] = int(child_volume_size.text or "")
    child_volume_type = el.find("VolumeType")
    if child_volume_type is not None:
        out["volume_type"] = str(child_volume_type.text or "")
    return out
