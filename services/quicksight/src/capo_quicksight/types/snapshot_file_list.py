"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_file

SnapshotFileList: TypeAlias = list["capo_quicksight.types.snapshot_file.SnapshotFile"]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFileList) -> list:
    import capo_quicksight.types.snapshot_file

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.snapshot_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> SnapshotFileList:
    import capo_quicksight.types.snapshot_file

    out: SnapshotFileList = []
    for item in data:
        out.append(capo_quicksight.types.snapshot_file.deserialize_json(item))
    return out
