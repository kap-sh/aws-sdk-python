"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionTagRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.row_level_permission_tag_delimiter
    import aws_sdk_quicksight.types.session_tag_key
    import aws_sdk_quicksight.types.session_tag_value
    import aws_sdk_quicksight.types.string


class RowLevelPermissionTagRule(TypedDict):
    tag_key: "aws_sdk_quicksight.types.session_tag_key.SessionTagKey"
    """<p>The unique key for a tag.</p>"""
    column_name: "aws_sdk_quicksight.types.string.String"
    """<p>The column name that a tag key is assigned to.</p>"""
    tag_multi_value_delimiter: NotRequired[
        "aws_sdk_quicksight.types.row_level_permission_tag_delimiter.RowLevelPermissionTagDelimiter"
    ]
    """<p>A string that you want to use to delimit the values when you pass the values at run time. For example, you can delimit the values with a comma.</p>"""
    match_all_value: NotRequired[
        "aws_sdk_quicksight.types.session_tag_value.SessionTagValue"
    ]
    """<p>A string that you want to use to filter by all the values in a column in the dataset and don’t want to list the values one by one. For example, you can use an asterisk as your match all value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionTagRule) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    out["ColumnName"] = value["column_name"]
    if "tag_multi_value_delimiter" in value:
        out["TagMultiValueDelimiter"] = value["tag_multi_value_delimiter"]
    if "match_all_value" in value:
        out["MatchAllValue"] = value["match_all_value"]
    return out


def deserialize_json(data: dict) -> RowLevelPermissionTagRule:
    out: RowLevelPermissionTagRule = {}  # type: ignore[typeddict-item]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    else:
        raise DeserializationError("RowLevelPermissionTagRule.tag_key required")
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("RowLevelPermissionTagRule.column_name required")
    if "TagMultiValueDelimiter" in data:
        out["tag_multi_value_delimiter"] = data["TagMultiValueDelimiter"]
    if "MatchAllValue" in data:
        out["match_all_value"] = data["MatchAllValue"]
    return out
