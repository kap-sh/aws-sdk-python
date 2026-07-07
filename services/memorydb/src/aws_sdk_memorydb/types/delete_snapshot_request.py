"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string


class DeleteSnapshotRequest(TypedDict, closed=True):
    snapshot_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the snapshot to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotRequest) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotRequest:
    out: DeleteSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "SnapshotName" in data:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        raise DeserializationError("DeleteSnapshotRequest.snapshot_name required")
    return out
