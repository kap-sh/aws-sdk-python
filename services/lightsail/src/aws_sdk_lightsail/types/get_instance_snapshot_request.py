"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class GetInstanceSnapshotRequest(TypedDict):
    instance_snapshot_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the snapshot for which you are requesting information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceSnapshotRequest) -> dict:
    out: dict = {}
    out["instanceSnapshotName"] = value["instance_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceSnapshotRequest:
    out: GetInstanceSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "instanceSnapshotName" in data:
        out["instance_snapshot_name"] = data["instanceSnapshotName"]
    else:
        raise DeserializationError(
            "GetInstanceSnapshotRequest.instance_snapshot_name required"
        )
    return out
