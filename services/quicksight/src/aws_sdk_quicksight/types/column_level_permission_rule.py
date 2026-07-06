"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnLevelPermissionRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_level_permission_rule_column_name_list
    import aws_sdk_quicksight.types.principal_list


class ColumnLevelPermissionRule(TypedDict, closed=True):
    principals: NotRequired["aws_sdk_quicksight.types.principal_list.PrincipalList"]
    """<p>An array of Amazon Resource Names (ARNs) for Quick Sight users or groups.</p>"""
    column_names: NotRequired[
        "aws_sdk_quicksight.types.column_level_permission_rule_column_name_list.ColumnLevelPermissionRuleColumnNameList"
    ]
    """<p>An array of column names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnLevelPermissionRule) -> dict:
    out: dict = {}
    if "principals" in value:
        import aws_sdk_quicksight.types.principal_list

        out["Principals"] = aws_sdk_quicksight.types.principal_list.serialize_json(
            value["principals"]
        )
    if "column_names" in value:
        import aws_sdk_quicksight.types.column_level_permission_rule_column_name_list

        out["ColumnNames"] = (
            aws_sdk_quicksight.types.column_level_permission_rule_column_name_list.serialize_json(
                value["column_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnLevelPermissionRule:
    out: ColumnLevelPermissionRule = {}  # type: ignore[typeddict-item]
    if "Principals" in data:
        import aws_sdk_quicksight.types.principal_list

        out["principals"] = aws_sdk_quicksight.types.principal_list.deserialize_json(
            data["Principals"]
        )
    if "ColumnNames" in data:
        import aws_sdk_quicksight.types.column_level_permission_rule_column_name_list

        out["column_names"] = (
            aws_sdk_quicksight.types.column_level_permission_rule_column_name_list.deserialize_json(
                data["ColumnNames"]
            )
        )
    return out
