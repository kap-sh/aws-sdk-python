"""Generated from Smithy shape ``com.amazonaws.quicksight#DatabaseGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.database_group

DatabaseGroupList: TypeAlias = list[
    "capo_quicksight.types.database_group.DatabaseGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseGroupList) -> list:
    return list(value)


def deserialize_json(data: list) -> DatabaseGroupList:
    return list(data)
