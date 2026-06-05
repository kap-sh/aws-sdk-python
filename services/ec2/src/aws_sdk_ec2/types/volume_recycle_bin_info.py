"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeRecycleBinInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_id
    import aws_sdk_ec2.types.volume_state
    import aws_sdk_ec2.types.volume_type


class VolumeRecycleBinInfo(TypedDict):
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume.</p>"""
    volume_type: NotRequired["aws_sdk_ec2.types.volume_type.VolumeType"]
    """<p>The volume type.</p>"""
    state: NotRequired["aws_sdk_ec2.types.volume_state.VolumeState"]
    """<p>The state of the volume.</p>"""
    size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p>"""
    iops: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) for the volume.</p>"""
    throughput: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Outpost on which the volume is stored. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-outposts.html\">Amazon EBS volumes on Outposts</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone for the volume.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone for the volume.</p>"""
    source_volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the source volume.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The snapshot from which the volume was created, if applicable.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the volume.</p>"""
    create_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time stamp when volume creation was initiated.</p>"""
    recycle_bin_enter_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the volume entered the Recycle Bin.</p>"""
    recycle_bin_exit_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the volume is to be permanently deleted from the Recycle Bin.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeRecycleBinInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "volume_id" in value:
        pairs.append((f"{prefix}.VolumeId", str(value["volume_id"])))
    if "volume_type" in value:
        import aws_sdk_ec2.types.volume_type

        aws_sdk_ec2.types.volume_type.serialize_ec2_query(
            value["volume_type"], pairs, f"{prefix}.VolumeType"
        )
    if "state" in value:
        import aws_sdk_ec2.types.volume_state

        aws_sdk_ec2.types.volume_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "size" in value:
        pairs.append((f"{prefix}.Size", str(value["size"])))
    if "iops" in value:
        pairs.append((f"{prefix}.Iops", str(value["iops"])))
    if "throughput" in value:
        pairs.append((f"{prefix}.Throughput", str(value["throughput"])))
    if "outpost_arn" in value:
        pairs.append((f"{prefix}.OutpostArn", str(value["outpost_arn"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "source_volume_id" in value:
        pairs.append((f"{prefix}.SourceVolumeId", str(value["source_volume_id"])))
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "operator" in value:
        import aws_sdk_ec2.types.operator_response

        aws_sdk_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{prefix}.Operator"
        )
    if "create_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{prefix}.CreateTime"
        )
    if "recycle_bin_enter_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_enter_time"], pairs, f"{prefix}.RecycleBinEnterTime"
        )
    if "recycle_bin_exit_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_exit_time"], pairs, f"{prefix}.RecycleBinExitTime"
        )


def deserialize_ec2_query(el: Element) -> VolumeRecycleBinInfo:
    out: VolumeRecycleBinInfo = {}  # type: ignore[typeddict-item]
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_volume_type = el.find("VolumeType")
    if child_volume_type is not None:
        import aws_sdk_ec2.types.volume_type

        out["volume_type"] = aws_sdk_ec2.types.volume_type.deserialize_ec2_query(
            child_volume_type
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.volume_state

        out["state"] = aws_sdk_ec2.types.volume_state.deserialize_ec2_query(child_state)
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_throughput = el.find("Throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_source_volume_id = el.find("SourceVolumeId")
    if child_source_volume_id is not None:
        out["source_volume_id"] = str(child_source_volume_id.text or "")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_operator = el.find("Operator")
    if child_operator is not None:
        import aws_sdk_ec2.types.operator_response

        out["operator"] = aws_sdk_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_ec2.types.date_time

        out["create_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_create_time
        )
    child_recycle_bin_enter_time = el.find("RecycleBinEnterTime")
    if child_recycle_bin_enter_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["recycle_bin_enter_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_enter_time
            )
        )
    child_recycle_bin_exit_time = el.find("RecycleBinExitTime")
    if child_recycle_bin_exit_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["recycle_bin_exit_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_exit_time
            )
        )
    return out
