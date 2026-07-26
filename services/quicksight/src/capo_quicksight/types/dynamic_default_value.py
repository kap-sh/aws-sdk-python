"""Generated from Smithy shape ``com.amazonaws.quicksight#DynamicDefaultValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier


class DynamicDefaultValue(TypedDict, closed=True):
    user_name_column: NotRequired[
        "capo_quicksight.types.column_identifier.ColumnIdentifier"
    ]
    """<p>The column that contains the username.</p>"""
    group_name_column: NotRequired[
        "capo_quicksight.types.column_identifier.ColumnIdentifier"
    ]
    """<p>The column that contains the group name.</p>"""
    default_value_column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that contains the default value of each user or group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynamicDefaultValue) -> dict:
    out: dict = {}
    if "user_name_column" in value:
        import capo_quicksight.types.column_identifier

        out["UserNameColumn"] = capo_quicksight.types.column_identifier.serialize_json(
            value["user_name_column"]
        )
    if "group_name_column" in value:
        import capo_quicksight.types.column_identifier

        out["GroupNameColumn"] = capo_quicksight.types.column_identifier.serialize_json(
            value["group_name_column"]
        )
    import capo_quicksight.types.column_identifier

    out["DefaultValueColumn"] = capo_quicksight.types.column_identifier.serialize_json(
        value["default_value_column"]
    )
    return out


def deserialize_json(data: dict) -> DynamicDefaultValue:
    out: DynamicDefaultValue = {}  # type: ignore[typeddict-item]
    if "UserNameColumn" in data:
        import capo_quicksight.types.column_identifier

        out["user_name_column"] = (
            capo_quicksight.types.column_identifier.deserialize_json(
                data["UserNameColumn"]
            )
        )
    if "GroupNameColumn" in data:
        import capo_quicksight.types.column_identifier

        out["group_name_column"] = (
            capo_quicksight.types.column_identifier.deserialize_json(
                data["GroupNameColumn"]
            )
        )
    if "DefaultValueColumn" in data:
        import capo_quicksight.types.column_identifier

        out["default_value_column"] = (
            capo_quicksight.types.column_identifier.deserialize_json(
                data["DefaultValueColumn"]
            )
        )
    else:
        raise DeserializationError("DynamicDefaultValue.default_value_column required")
    return out
