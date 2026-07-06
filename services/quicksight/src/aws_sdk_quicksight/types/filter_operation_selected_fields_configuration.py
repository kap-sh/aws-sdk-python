"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterOperationSelectedFieldsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_action_column_list
    import aws_sdk_quicksight.types.selected_field_list
    import aws_sdk_quicksight.types.selected_field_options


class FilterOperationSelectedFieldsConfiguration(TypedDict, closed=True):
    selected_fields: NotRequired[
        "aws_sdk_quicksight.types.selected_field_list.SelectedFieldList"
    ]
    """<p>Chooses the fields that are filtered in <code>CustomActionFilterOperation</code>.</p>"""
    selected_field_options: NotRequired[
        "aws_sdk_quicksight.types.selected_field_options.SelectedFieldOptions"
    ]
    """<p>A structure that contains the options that choose which fields are filtered in the <code>CustomActionFilterOperation</code>.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>ALL_FIELDS</code>: Applies the filter operation to all fields.</p> </li> </ul>"""
    selected_columns: NotRequired[
        "aws_sdk_quicksight.types.custom_action_column_list.CustomActionColumnList"
    ]
    """<p>The selected columns of a dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperationSelectedFieldsConfiguration) -> dict:
    out: dict = {}
    if "selected_fields" in value:
        import aws_sdk_quicksight.types.selected_field_list

        out["SelectedFields"] = (
            aws_sdk_quicksight.types.selected_field_list.serialize_json(
                value["selected_fields"]
            )
        )
    if "selected_field_options" in value:
        import aws_sdk_quicksight.types.selected_field_options

        out["SelectedFieldOptions"] = (
            aws_sdk_quicksight.types.selected_field_options.serialize_json(
                value["selected_field_options"]
            )
        )
    if "selected_columns" in value:
        import aws_sdk_quicksight.types.custom_action_column_list

        out["SelectedColumns"] = (
            aws_sdk_quicksight.types.custom_action_column_list.serialize_json(
                value["selected_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterOperationSelectedFieldsConfiguration:
    out: FilterOperationSelectedFieldsConfiguration = {}  # type: ignore[typeddict-item]
    if "SelectedFields" in data:
        import aws_sdk_quicksight.types.selected_field_list

        out["selected_fields"] = (
            aws_sdk_quicksight.types.selected_field_list.deserialize_json(
                data["SelectedFields"]
            )
        )
    if "SelectedFieldOptions" in data:
        import aws_sdk_quicksight.types.selected_field_options

        out["selected_field_options"] = (
            aws_sdk_quicksight.types.selected_field_options.deserialize_json(
                data["SelectedFieldOptions"]
            )
        )
    if "SelectedColumns" in data:
        import aws_sdk_quicksight.types.custom_action_column_list

        out["selected_columns"] = (
            aws_sdk_quicksight.types.custom_action_column_list.deserialize_json(
                data["SelectedColumns"]
            )
        )
    return out
