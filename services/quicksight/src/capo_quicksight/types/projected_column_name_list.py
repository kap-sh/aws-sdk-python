"""Generated from Smithy shape ``com.amazonaws.quicksight#ProjectedColumnNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.string

ProjectedColumnNameList: TypeAlias = list["capo_quicksight.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectedColumnNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ProjectedColumnNameList:
    return list(data)
