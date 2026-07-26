"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDiskSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.tag_list


class CreateDiskSnapshotRequest(TypedDict, closed=True):
    disk_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The unique name of the source disk (<code>Disk-Virginia-1</code>).</p> <note> <p>This parameter cannot be defined together with the <code>instance name</code> parameter. The <code>disk name</code> and <code>instance name</code> parameters are mutually exclusive.</p> </note>"""
    disk_snapshot_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the destination disk snapshot (<code>my-disk-snapshot</code>) based on the source disk.</p>"""
    instance_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The unique name of the source instance (<code>Amazon_Linux-512MB-Virginia-1</code>). When this is defined, a snapshot of the instance's system volume is created.</p> <note> <p>This parameter cannot be defined together with the <code>disk name</code> parameter. The <code>instance name</code> and <code>disk name</code> parameters are mutually exclusive.</p> </note>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDiskSnapshotRequest) -> dict:
    out: dict = {}
    if "disk_name" in value:
        out["diskName"] = value["disk_name"]
    out["diskSnapshotName"] = value["disk_snapshot_name"]
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDiskSnapshotRequest:
    out: CreateDiskSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "diskName" in data:
        out["disk_name"] = data["diskName"]
    if "diskSnapshotName" in data:
        out["disk_snapshot_name"] = data["diskSnapshotName"]
    else:
        raise DeserializationError(
            "CreateDiskSnapshotRequest.disk_snapshot_name required"
        )
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    if "tags" in data:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
