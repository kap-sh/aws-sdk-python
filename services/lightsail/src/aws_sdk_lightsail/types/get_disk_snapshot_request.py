"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDiskSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class GetDiskSnapshotRequest(TypedDict):
    disk_snapshot_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the disk snapshot (<code>my-disk-snapshot</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiskSnapshotRequest) -> dict:
    out: dict = {}
    out["diskSnapshotName"] = value["disk_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiskSnapshotRequest:
    out: GetDiskSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "diskSnapshotName" in data:
        out["disk_snapshot_name"] = data["diskSnapshotName"]
    else:
        raise DeserializationError("GetDiskSnapshotRequest.disk_snapshot_name required")
    return out
