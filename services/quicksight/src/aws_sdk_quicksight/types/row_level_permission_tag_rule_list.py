"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionTagRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.row_level_permission_tag_rule

RowLevelPermissionTagRuleList: TypeAlias = list[
    "aws_sdk_quicksight.types.row_level_permission_tag_rule.RowLevelPermissionTagRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionTagRuleList) -> list:
    import aws_sdk_quicksight.types.row_level_permission_tag_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.row_level_permission_tag_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RowLevelPermissionTagRuleList:
    import aws_sdk_quicksight.types.row_level_permission_tag_rule

    out: RowLevelPermissionTagRuleList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.row_level_permission_tag_rule.deserialize_json(
                item
            )
        )
    return out
