"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnLevelPermissionRuleColumnNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.string

ColumnLevelPermissionRuleColumnNameList: TypeAlias = list[
    "capo_quicksight.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnLevelPermissionRuleColumnNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ColumnLevelPermissionRuleColumnNameList:
    return list(data)
