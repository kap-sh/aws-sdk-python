"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.string

FolderColumnList: TypeAlias = list["capo_quicksight.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: FolderColumnList) -> list:
    return list(value)


def deserialize_json(data: list) -> FolderColumnList:
    return list(data)
