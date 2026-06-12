"""Generated from Smithy shape ``com.amazonaws.lightsail#ExportSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class ExportSnapshotRequest(TypedDict):
    source_snapshot_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance or disk snapshot to be exported to Amazon EC2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSnapshotRequest) -> dict:
    out: dict = {}
    out["sourceSnapshotName"] = value["source_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportSnapshotRequest:
    out: ExportSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "sourceSnapshotName" in data:
        out["source_snapshot_name"] = data["sourceSnapshotName"]
    else:
        raise DeserializationError(
            "ExportSnapshotRequest.source_snapshot_name required"
        )
    return out
