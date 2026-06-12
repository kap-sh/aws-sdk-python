"""Generated from Smithy shape ``com.amazonaws.workspaces#Snapshot``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.timestamp


class Snapshot(TypedDict):
    snapshot_time: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The time when the snapshot was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshot) -> dict:
    out: dict = {}
    if "snapshot_time" in value:
        import aws_sdk_workspaces.types.timestamp

        out["SnapshotTime"] = aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["snapshot_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if "SnapshotTime" in data:
        import aws_sdk_workspaces.types.timestamp

        out["snapshot_time"] = (
            aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["SnapshotTime"]
            )
        )
    return out
