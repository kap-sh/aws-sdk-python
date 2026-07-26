"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionTagRuleConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.row_level_permission_tag_rule_configuration

RowLevelPermissionTagRuleConfigurationList: TypeAlias = list[
    "capo_quicksight.types.row_level_permission_tag_rule_configuration.RowLevelPermissionTagRuleConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionTagRuleConfigurationList) -> list:
    import capo_quicksight.types.row_level_permission_tag_rule_configuration

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.row_level_permission_tag_rule_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RowLevelPermissionTagRuleConfigurationList:
    import capo_quicksight.types.row_level_permission_tag_rule_configuration

    out: RowLevelPermissionTagRuleConfigurationList = []
    for item in data:
        out.append(
            capo_quicksight.types.row_level_permission_tag_rule_configuration.deserialize_json(
                item
            )
        )
    return out
