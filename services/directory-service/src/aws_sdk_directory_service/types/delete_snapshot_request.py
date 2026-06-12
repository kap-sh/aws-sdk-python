"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.snapshot_id


class DeleteSnapshotRequest(TypedDict):
    snapshot_id: "aws_sdk_directory_service.types.snapshot_id.SnapshotId"
    """<p>The identifier of the directory snapshot to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotRequest) -> dict:
    out: dict = {}
    out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotRequest:
    out: DeleteSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    else:
        raise DeserializationError("DeleteSnapshotRequest.snapshot_id required")
    return out
