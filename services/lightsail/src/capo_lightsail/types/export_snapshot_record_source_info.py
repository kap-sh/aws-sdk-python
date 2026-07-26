"""Generated from Smithy shape ``com.amazonaws.lightsail#ExportSnapshotRecordSourceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.disk_snapshot_info
    import capo_lightsail.types.export_snapshot_record_source_type
    import capo_lightsail.types.instance_snapshot_info
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string


class ExportSnapshotRecordSourceInfo(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_lightsail.types.export_snapshot_record_source_type.ExportSnapshotRecordSourceType"
    ]
    """<p>The Lightsail resource type (<code>InstanceSnapshot</code> or <code>DiskSnapshot</code>).</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The date when the source instance or disk snapshot was created.</p>"""
    name: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The name of the source instance or disk snapshot.</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the source instance or disk snapshot.</p>"""
    from_resource_name: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the snapshot's source instance or disk.</p>"""
    from_resource_arn: NotRequired[
        "capo_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the snapshot's source instance or disk.</p>"""
    instance_snapshot_info: NotRequired[
        "capo_lightsail.types.instance_snapshot_info.InstanceSnapshotInfo"
    ]
    """<p>A list of objects describing an instance snapshot.</p>"""
    disk_snapshot_info: NotRequired[
        "capo_lightsail.types.disk_snapshot_info.DiskSnapshotInfo"
    ]
    """<p>A list of objects describing a disk snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSnapshotRecordSourceInfo) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_lightsail.types.export_snapshot_record_source_type

        out["resourceType"] = (
            capo_lightsail.types.export_snapshot_record_source_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "from_resource_name" in value:
        out["fromResourceName"] = value["from_resource_name"]
    if "from_resource_arn" in value:
        out["fromResourceArn"] = value["from_resource_arn"]
    if "instance_snapshot_info" in value:
        import capo_lightsail.types.instance_snapshot_info

        out["instanceSnapshotInfo"] = (
            capo_lightsail.types.instance_snapshot_info.serialize_aws_json_1_1(
                value["instance_snapshot_info"]
            )
        )
    if "disk_snapshot_info" in value:
        import capo_lightsail.types.disk_snapshot_info

        out["diskSnapshotInfo"] = (
            capo_lightsail.types.disk_snapshot_info.serialize_aws_json_1_1(
                value["disk_snapshot_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportSnapshotRecordSourceInfo:
    out: ExportSnapshotRecordSourceInfo = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import capo_lightsail.types.export_snapshot_record_source_type

        out["resource_type"] = (
            capo_lightsail.types.export_snapshot_record_source_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "createdAt" in data:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "fromResourceName" in data:
        out["from_resource_name"] = data["fromResourceName"]
    if "fromResourceArn" in data:
        out["from_resource_arn"] = data["fromResourceArn"]
    if "instanceSnapshotInfo" in data:
        import capo_lightsail.types.instance_snapshot_info

        out["instance_snapshot_info"] = (
            capo_lightsail.types.instance_snapshot_info.deserialize_aws_json_1_1(
                data["instanceSnapshotInfo"]
            )
        )
    if "diskSnapshotInfo" in data:
        import capo_lightsail.types.disk_snapshot_info

        out["disk_snapshot_info"] = (
            capo_lightsail.types.disk_snapshot_info.deserialize_aws_json_1_1(
                data["diskSnapshotInfo"]
            )
        )
    return out
