"""Generated from Smithy shape ``com.amazonaws.lightsail#AutoSnapshotDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.attached_disk_list
    import aws_sdk_lightsail.types.auto_snapshot_status
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.string


class AutoSnapshotDetails(TypedDict, closed=True):
    date: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The date of the automatic snapshot in <code>YYYY-MM-DD</code> format.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the automatic snapshot was created.</p>"""
    status: NotRequired[
        "aws_sdk_lightsail.types.auto_snapshot_status.AutoSnapshotStatus"
    ]
    """<p>The status of the automatic snapshot.</p>"""
    from_attached_disks: NotRequired[
        "aws_sdk_lightsail.types.attached_disk_list.AttachedDiskList"
    ]
    """<p>An array of objects that describe the block storage disks attached to the instance when the automatic snapshot was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoSnapshotDetails) -> dict:
    out: dict = {}
    if "date" in value:
        out["date"] = value["date"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "status" in value:
        import aws_sdk_lightsail.types.auto_snapshot_status

        out["status"] = (
            aws_sdk_lightsail.types.auto_snapshot_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "from_attached_disks" in value:
        import aws_sdk_lightsail.types.attached_disk_list

        out["fromAttachedDisks"] = (
            aws_sdk_lightsail.types.attached_disk_list.serialize_aws_json_1_1(
                value["from_attached_disks"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoSnapshotDetails:
    out: AutoSnapshotDetails = {}  # type: ignore[typeddict-item]
    if "date" in data:
        out["date"] = data["date"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "status" in data:
        import aws_sdk_lightsail.types.auto_snapshot_status

        out["status"] = (
            aws_sdk_lightsail.types.auto_snapshot_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "fromAttachedDisks" in data:
        import aws_sdk_lightsail.types.attached_disk_list

        out["from_attached_disks"] = (
            aws_sdk_lightsail.types.attached_disk_list.deserialize_aws_json_1_1(
                data["fromAttachedDisks"]
            )
        )
    return out
