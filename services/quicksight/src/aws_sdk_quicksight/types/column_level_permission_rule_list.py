"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnLevelPermissionRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_level_permission_rule

ColumnLevelPermissionRuleList: TypeAlias = list[
    "aws_sdk_quicksight.types.column_level_permission_rule.ColumnLevelPermissionRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnLevelPermissionRuleList) -> list:
    import aws_sdk_quicksight.types.column_level_permission_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.column_level_permission_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ColumnLevelPermissionRuleList:
    import aws_sdk_quicksight.types.column_level_permission_rule

    out: ColumnLevelPermissionRuleList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.column_level_permission_rule.deserialize_json(item)
        )
    return out
