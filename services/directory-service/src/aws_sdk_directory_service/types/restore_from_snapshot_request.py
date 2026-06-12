"""Generated from Smithy shape ``com.amazonaws.directoryservice#RestoreFromSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.snapshot_id


class RestoreFromSnapshotRequest(TypedDict):
    snapshot_id: "aws_sdk_directory_service.types.snapshot_id.SnapshotId"
    """<p>The identifier of the snapshot to restore from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreFromSnapshotRequest) -> dict:
    out: dict = {}
    out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreFromSnapshotRequest:
    out: RestoreFromSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    else:
        raise DeserializationError("RestoreFromSnapshotRequest.snapshot_id required")
    return out
