"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

FolderArnList: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: FolderArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> FolderArnList:
    return list(data)
