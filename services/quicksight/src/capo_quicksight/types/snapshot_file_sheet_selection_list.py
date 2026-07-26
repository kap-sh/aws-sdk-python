"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileSheetSelectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_file_sheet_selection

SnapshotFileSheetSelectionList: TypeAlias = list[
    "capo_quicksight.types.snapshot_file_sheet_selection.SnapshotFileSheetSelection"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFileSheetSelectionList) -> list:
    import capo_quicksight.types.snapshot_file_sheet_selection

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.snapshot_file_sheet_selection.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SnapshotFileSheetSelectionList:
    import capo_quicksight.types.snapshot_file_sheet_selection

    out: SnapshotFileSheetSelectionList = []
    for item in data:
        out.append(
            capo_quicksight.types.snapshot_file_sheet_selection.deserialize_json(item)
        )
    return out
