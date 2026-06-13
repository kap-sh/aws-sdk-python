"""Generated from Smithy shape ``com.amazonaws.quicksight#DynamicDefaultValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier


class DynamicDefaultValue(TypedDict):
    user_name_column: NotRequired[
        "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    ]
    """<p>The column that contains the username.</p>"""
    group_name_column: NotRequired[
        "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    ]
    """<p>The column that contains the group name.</p>"""
    default_value_column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that contains the default value of each user or group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynamicDefaultValue) -> dict:
    out: dict = {}
    if "user_name_column" in value:
        import aws_sdk_quicksight.types.column_identifier

        out["UserNameColumn"] = (
            aws_sdk_quicksight.types.column_identifier.serialize_json(
                value["user_name_column"]
            )
        )
    if "group_name_column" in value:
        import aws_sdk_quicksight.types.column_identifier

        out["GroupNameColumn"] = (
            aws_sdk_quicksight.types.column_identifier.serialize_json(
                value["group_name_column"]
            )
        )
    import aws_sdk_quicksight.types.column_identifier

    out["DefaultValueColumn"] = (
        aws_sdk_quicksight.types.column_identifier.serialize_json(
            value["default_value_column"]
        )
    )
    return out


def deserialize_json(data: dict) -> DynamicDefaultValue:
    out: DynamicDefaultValue = {}  # type: ignore[typeddict-item]
    if "UserNameColumn" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["user_name_column"] = (
            aws_sdk_quicksight.types.column_identifier.deserialize_json(
                data["UserNameColumn"]
            )
        )
    if "GroupNameColumn" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["group_name_column"] = (
            aws_sdk_quicksight.types.column_identifier.deserialize_json(
                data["GroupNameColumn"]
            )
        )
    if "DefaultValueColumn" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["default_value_column"] = (
            aws_sdk_quicksight.types.column_identifier.deserialize_json(
                data["DefaultValueColumn"]
            )
        )
    else:
        raise DeserializationError("DynamicDefaultValue.default_value_column required")
    return out
