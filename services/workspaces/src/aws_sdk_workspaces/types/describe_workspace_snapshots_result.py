"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceSnapshotsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.snapshot_list


class DescribeWorkspaceSnapshotsResult(TypedDict):
    rebuild_snapshots: NotRequired[
        "aws_sdk_workspaces.types.snapshot_list.SnapshotList"
    ]
    """<p>Information about the snapshots that can be used to rebuild a WorkSpace. These snapshots include the user volume.</p>"""
    restore_snapshots: NotRequired[
        "aws_sdk_workspaces.types.snapshot_list.SnapshotList"
    ]
    """<p>Information about the snapshots that can be used to restore a WorkSpace. These snapshots include both the root volume and the user volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceSnapshotsResult) -> dict:
    out: dict = {}
    if "rebuild_snapshots" in value:
        import aws_sdk_workspaces.types.snapshot_list

        out["RebuildSnapshots"] = (
            aws_sdk_workspaces.types.snapshot_list.serialize_aws_json_1_1(
                value["rebuild_snapshots"]
            )
        )
    if "restore_snapshots" in value:
        import aws_sdk_workspaces.types.snapshot_list

        out["RestoreSnapshots"] = (
            aws_sdk_workspaces.types.snapshot_list.serialize_aws_json_1_1(
                value["restore_snapshots"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceSnapshotsResult:
    out: DescribeWorkspaceSnapshotsResult = {}  # type: ignore[typeddict-item]
    if "RebuildSnapshots" in data:
        import aws_sdk_workspaces.types.snapshot_list

        out["rebuild_snapshots"] = (
            aws_sdk_workspaces.types.snapshot_list.deserialize_aws_json_1_1(
                data["RebuildSnapshots"]
            )
        )
    if "RestoreSnapshots" in data:
        import aws_sdk_workspaces.types.snapshot_list

        out["restore_snapshots"] = (
            aws_sdk_workspaces.types.snapshot_list.deserialize_aws_json_1_1(
                data["RestoreSnapshots"]
            )
        )
    return out
