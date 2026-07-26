"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileSheetSelectionScope``."""

from typing import Literal, TypeAlias, cast

SnapshotFileSheetSelectionScope: TypeAlias = Literal[
    "ALL_VISUALS",
    "SELECTED_VISUALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFileSheetSelectionScope) -> str:
    return value


def deserialize_json(data: str) -> SnapshotFileSheetSelectionScope:
    return cast(SnapshotFileSheetSelectionScope, data)
