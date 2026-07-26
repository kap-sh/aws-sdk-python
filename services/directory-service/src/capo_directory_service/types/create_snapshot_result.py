"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.snapshot_id


class CreateSnapshotResult(TypedDict, closed=True):
    snapshot_id: NotRequired["capo_directory_service.types.snapshot_id.SnapshotId"]
    """<p>The identifier of the snapshot that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotResult) -> dict:
    out: dict = {}
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotResult:
    out: CreateSnapshotResult = {}  # type: ignore[typeddict-item]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    return out
