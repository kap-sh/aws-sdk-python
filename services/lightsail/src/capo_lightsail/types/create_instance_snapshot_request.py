"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateInstanceSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.tag_list


class CreateInstanceSnapshotRequest(TypedDict, closed=True):
    instance_snapshot_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name for your new snapshot.</p>"""
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The Lightsail instance on which to base your snapshot.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInstanceSnapshotRequest) -> dict:
    out: dict = {}
    out["instanceSnapshotName"] = value["instance_snapshot_name"]
    out["instanceName"] = value["instance_name"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInstanceSnapshotRequest:
    out: CreateInstanceSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "instanceSnapshotName" in data:
        out["instance_snapshot_name"] = data["instanceSnapshotName"]
    else:
        raise DeserializationError(
            "CreateInstanceSnapshotRequest.instance_snapshot_name required"
        )
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError(
            "CreateInstanceSnapshotRequest.instance_name required"
        )
    if "tags" in data:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
