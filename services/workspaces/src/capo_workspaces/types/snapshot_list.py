"""Generated from Smithy shape ``com.amazonaws.workspaces#SnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.snapshot

SnapshotList: TypeAlias = list["capo_workspaces.types.snapshot.Snapshot"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotList) -> list:
    import capo_workspaces.types.snapshot

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.snapshot.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SnapshotList:
    import capo_workspaces.types.snapshot

    out: SnapshotList = []
    for item in data:
        out.append(capo_workspaces.types.snapshot.deserialize_aws_json_1_1(item))
    return out
