"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileSheetSelectionVisualIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_restrictive_resource_id

SnapshotFileSheetSelectionVisualIdList: TypeAlias = list[
    "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFileSheetSelectionVisualIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SnapshotFileSheetSelectionVisualIdList:
    return list(data)
