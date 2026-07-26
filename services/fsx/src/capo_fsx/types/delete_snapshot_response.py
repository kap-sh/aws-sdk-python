"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.snapshot_id
    import capo_fsx.types.snapshot_lifecycle


class DeleteSnapshotResponse(TypedDict, closed=True):
    snapshot_id: NotRequired["capo_fsx.types.snapshot_id.SnapshotId"]
    """<p>The ID of the deleted snapshot.</p>"""
    lifecycle: NotRequired["capo_fsx.types.snapshot_lifecycle.SnapshotLifecycle"]
    """<p>The lifecycle status of the snapshot. If the <code>DeleteSnapshot</code> operation is successful, this status is <code>DELETING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "lifecycle" in value:
        import capo_fsx.types.snapshot_lifecycle

        out["Lifecycle"] = capo_fsx.types.snapshot_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotResponse:
    out: DeleteSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    if "Lifecycle" in data:
        import capo_fsx.types.snapshot_lifecycle

        out["lifecycle"] = capo_fsx.types.snapshot_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    return out
