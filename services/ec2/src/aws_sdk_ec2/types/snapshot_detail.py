"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.sensitive_url
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_bucket_details


class SnapshotDetail(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the snapshot.</p>"""
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The block device mapping for the snapshot.</p>"""
    disk_image_size: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The size of the disk in the snapshot, in GiB.</p>"""
    format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The format of the disk image from which the snapshot is created.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The percentage of progress for the task.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The snapshot ID of the disk being imported.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief status of the snapshot creation.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A detailed status message for the snapshot creation.</p>"""
    url: NotRequired["aws_sdk_ec2.types.sensitive_url.SensitiveUrl"]
    """<p>The URL used to access the disk image.</p>"""
    user_bucket: NotRequired["aws_sdk_ec2.types.user_bucket_details.UserBucketDetails"]
    """<p>The Amazon S3 bucket for the disk image.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "device_name" in value:
        pairs.append((f"{prefix}.DeviceName", str(value["device_name"])))
    if "disk_image_size" in value:
        pairs.append((f"{prefix}.DiskImageSize", str(value["disk_image_size"])))
    if "format" in value:
        pairs.append((f"{prefix}.Format", str(value["format"])))
    if "progress" in value:
        pairs.append((f"{prefix}.Progress", str(value["progress"])))
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "url" in value:
        pairs.append((f"{prefix}.Url", str(value["url"])))
    if "user_bucket" in value:
        import aws_sdk_ec2.types.user_bucket_details

        aws_sdk_ec2.types.user_bucket_details.serialize_ec2_query(
            value["user_bucket"], pairs, f"{prefix}.UserBucket"
        )


def deserialize_ec2_query(el: Element) -> SnapshotDetail:
    out: SnapshotDetail = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_disk_image_size = el.find("DiskImageSize")
    if child_disk_image_size is not None:
        out["disk_image_size"] = float(child_disk_image_size.text or "")
    child_format = el.find("Format")
    if child_format is not None:
        out["format"] = str(child_format.text or "")
    child_progress = el.find("Progress")
    if child_progress is not None:
        out["progress"] = str(child_progress.text or "")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_url = el.find("Url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    child_user_bucket = el.find("UserBucket")
    if child_user_bucket is not None:
        import aws_sdk_ec2.types.user_bucket_details

        out["user_bucket"] = (
            aws_sdk_ec2.types.user_bucket_details.deserialize_ec2_query(
                child_user_bucket
            )
        )
    return out
