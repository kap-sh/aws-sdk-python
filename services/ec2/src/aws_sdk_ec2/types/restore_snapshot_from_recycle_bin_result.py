"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreSnapshotFromRecycleBinResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.snapshot_state
    import aws_sdk_ec2.types.sse_type
    import aws_sdk_ec2.types.string


class RestoreSnapshotFromRecycleBinResult(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Outpost on which the snapshot is stored. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html\">Amazon EBS local snapshots on Outposts</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the snapshot.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is encrypted.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the EBS snapshot.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The progress of the snapshot, as a percentage.</p>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time stamp when the snapshot was initiated.</p>"""
    state: NotRequired["aws_sdk_ec2.types.snapshot_state.SnapshotState"]
    """<p>The state of the snapshot.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the volume that was used to create the snapshot.</p>"""
    volume_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p>"""
    sse_type: NotRequired["aws_sdk_ec2.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RestoreSnapshotFromRecycleBinResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "outpost_arn" in value:
        pairs.append((f"{prefix}.OutpostArn", str(value["outpost_arn"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "encrypted" in value:
        pairs.append((f"{prefix}.Encrypted", "true" if value["encrypted"] else "false"))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "progress" in value:
        pairs.append((f"{prefix}.Progress", str(value["progress"])))
    if "start_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "state" in value:
        import aws_sdk_ec2.types.snapshot_state

        aws_sdk_ec2.types.snapshot_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.Status"
        )
    if "volume_id" in value:
        pairs.append((f"{prefix}.VolumeId", str(value["volume_id"])))
    if "volume_size" in value:
        pairs.append((f"{prefix}.VolumeSize", str(value["volume_size"])))
    if "sse_type" in value:
        import aws_sdk_ec2.types.sse_type

        aws_sdk_ec2.types.sse_type.serialize_ec2_query(
            value["sse_type"], pairs, f"{prefix}.SseType"
        )


def deserialize_ec2_query(el: Element) -> RestoreSnapshotFromRecycleBinResult:
    out: RestoreSnapshotFromRecycleBinResult = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_progress = el.find("Progress")
    if child_progress is not None:
        out["progress"] = str(child_progress.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["start_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_start_time
            )
        )
    child_state = el.find("Status")
    if child_state is not None:
        import aws_sdk_ec2.types.snapshot_state

        out["state"] = aws_sdk_ec2.types.snapshot_state.deserialize_ec2_query(
            child_state
        )
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_volume_size = el.find("VolumeSize")
    if child_volume_size is not None:
        out["volume_size"] = int(child_volume_size.text or "")
    child_sse_type = el.find("SseType")
    if child_sse_type is not None:
        import aws_sdk_ec2.types.sse_type

        out["sse_type"] = aws_sdk_ec2.types.sse_type.deserialize_ec2_query(
            child_sse_type
        )
    return out
