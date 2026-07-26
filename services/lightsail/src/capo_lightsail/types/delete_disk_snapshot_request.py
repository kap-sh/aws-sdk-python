"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteDiskSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class DeleteDiskSnapshotRequest(TypedDict, closed=True):
    disk_snapshot_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the disk snapshot you want to delete (<code>my-disk-snapshot</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDiskSnapshotRequest) -> dict:
    out: dict = {}
    out["diskSnapshotName"] = value["disk_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDiskSnapshotRequest:
    out: DeleteDiskSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "diskSnapshotName" in data:
        out["disk_snapshot_name"] = data["diskSnapshotName"]
    else:
        raise DeserializationError(
            "DeleteDiskSnapshotRequest.disk_snapshot_name required"
        )
    return out
