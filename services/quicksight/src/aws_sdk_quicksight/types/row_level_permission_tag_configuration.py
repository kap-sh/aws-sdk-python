"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionTagConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.row_level_permission_tag_rule_configuration_list
    import aws_sdk_quicksight.types.row_level_permission_tag_rule_list
    import aws_sdk_quicksight.types.status


class RowLevelPermissionTagConfiguration(TypedDict):
    status: NotRequired["aws_sdk_quicksight.types.status.Status"]
    """<p>The status of row-level security tags. If enabled, the status is <code>ENABLED</code>. If disabled, the status is <code>DISABLED</code>.</p>"""
    tag_rules: "aws_sdk_quicksight.types.row_level_permission_tag_rule_list.RowLevelPermissionTagRuleList"
    """<p>A set of rules associated with row-level security, such as the tag names and columns that they are assigned to.</p>"""
    tag_rule_configurations: NotRequired[
        "aws_sdk_quicksight.types.row_level_permission_tag_rule_configuration_list.RowLevelPermissionTagRuleConfigurationList"
    ]
    """<p>A list of tag configuration rules to apply to a dataset. All tag configurations have the OR condition. Tags within each tile will be joined (AND). At least one rule in this structure must have all tag values assigned to it to apply Row-level security (RLS) to the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionTagConfiguration) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_quicksight.types.status

        out["Status"] = aws_sdk_quicksight.types.status.serialize_json(value["status"])
    import aws_sdk_quicksight.types.row_level_permission_tag_rule_list

    out["TagRules"] = (
        aws_sdk_quicksight.types.row_level_permission_tag_rule_list.serialize_json(
            value["tag_rules"]
        )
    )
    if "tag_rule_configurations" in value:
        import aws_sdk_quicksight.types.row_level_permission_tag_rule_configuration_list

        out["TagRuleConfigurations"] = (
            aws_sdk_quicksight.types.row_level_permission_tag_rule_configuration_list.serialize_json(
                value["tag_rule_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> RowLevelPermissionTagConfiguration:
    out: RowLevelPermissionTagConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_quicksight.types.status

        out["status"] = aws_sdk_quicksight.types.status.deserialize_json(data["Status"])
    if "TagRules" in data:
        import aws_sdk_quicksight.types.row_level_permission_tag_rule_list

        out["tag_rules"] = (
            aws_sdk_quicksight.types.row_level_permission_tag_rule_list.deserialize_json(
                data["TagRules"]
            )
        )
    else:
        raise DeserializationError(
            "RowLevelPermissionTagConfiguration.tag_rules required"
        )
    if "TagRuleConfigurations" in data:
        import aws_sdk_quicksight.types.row_level_permission_tag_rule_configuration_list

        out["tag_rule_configurations"] = (
            aws_sdk_quicksight.types.row_level_permission_tag_rule_configuration_list.deserialize_json(
                data["TagRuleConfigurations"]
            )
        )
    return out
