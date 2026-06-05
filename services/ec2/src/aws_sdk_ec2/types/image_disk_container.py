"""Generated from Smithy shape ``com.amazonaws.ec2#ImageDiskContainer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.sensitive_url
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_bucket


class ImageDiskContainer(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the disk image.</p>"""
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The block device mapping for the disk.</p>"""
    format: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The format of the disk image being imported.</p> <p>Valid values: <code>OVA</code> | <code>VHD</code> | <code>VHDX</code> | <code>VMDK</code> | <code>RAW</code> </p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the EBS snapshot to be used for importing the snapshot.</p>"""
    url: NotRequired["aws_sdk_ec2.types.sensitive_url.SensitiveUrl"]
    """<p>The URL to the Amazon S3-based disk image being imported. The URL can either be a https URL (https://..) or an Amazon S3 URL (s3://..)</p>"""
    user_bucket: NotRequired["aws_sdk_ec2.types.user_bucket.UserBucket"]
    """<p>The S3 bucket for the disk image.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageDiskContainer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "device_name" in value:
        pairs.append((f"{prefix}.DeviceName", str(value["device_name"])))
    if "format" in value:
        pairs.append((f"{prefix}.Format", str(value["format"])))
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "url" in value:
        pairs.append((f"{prefix}.Url", str(value["url"])))
    if "user_bucket" in value:
        import aws_sdk_ec2.types.user_bucket

        aws_sdk_ec2.types.user_bucket.serialize_ec2_query(
            value["user_bucket"], pairs, f"{prefix}.UserBucket"
        )


def deserialize_ec2_query(el: Element) -> ImageDiskContainer:
    out: ImageDiskContainer = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_format = el.find("Format")
    if child_format is not None:
        out["format"] = str(child_format.text or "")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_url = el.find("Url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    child_user_bucket = el.find("UserBucket")
    if child_user_bucket is not None:
        import aws_sdk_ec2.types.user_bucket

        out["user_bucket"] = aws_sdk_ec2.types.user_bucket.deserialize_ec2_query(
            child_user_bucket
        )
    return out
