"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_file_group

SnapshotFileGroupList: TypeAlias = list[
    "capo_quicksight.types.snapshot_file_group.SnapshotFileGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFileGroupList) -> list:
    import capo_quicksight.types.snapshot_file_group

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.snapshot_file_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> SnapshotFileGroupList:
    import capo_quicksight.types.snapshot_file_group

    out: SnapshotFileGroupList = []
    for item in data:
        out.append(capo_quicksight.types.snapshot_file_group.deserialize_json(item))
    return out
