"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_order_list
    import aws_sdk_quicksight.types.table_field_option_list
    import aws_sdk_quicksight.types.table_pinned_field_options
    import aws_sdk_quicksight.types.transposed_table_option_list


class TableFieldOptions(TypedDict):
    selected_field_options: NotRequired[
        "aws_sdk_quicksight.types.table_field_option_list.TableFieldOptionList"
    ]
    """<p>The field options to be configured to a table.</p>"""
    order: NotRequired["aws_sdk_quicksight.types.field_order_list.FieldOrderList"]
    """<p>The order of the field IDs that are configured as field options for a table visual.</p>"""
    pinned_field_options: NotRequired[
        "aws_sdk_quicksight.types.table_pinned_field_options.TablePinnedFieldOptions"
    ]
    """<p>The settings for the pinned columns of a table visual.</p>"""
    transposed_table_options: NotRequired[
        "aws_sdk_quicksight.types.transposed_table_option_list.TransposedTableOptionList"
    ]
    """<p>The <code>TableOptions</code> of a transposed table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldOptions) -> dict:
    out: dict = {}
    if "selected_field_options" in value:
        import aws_sdk_quicksight.types.table_field_option_list

        out["SelectedFieldOptions"] = (
            aws_sdk_quicksight.types.table_field_option_list.serialize_json(
                value["selected_field_options"]
            )
        )
    if "order" in value:
        import aws_sdk_quicksight.types.field_order_list

        out["Order"] = aws_sdk_quicksight.types.field_order_list.serialize_json(
            value["order"]
        )
    if "pinned_field_options" in value:
        import aws_sdk_quicksight.types.table_pinned_field_options

        out["PinnedFieldOptions"] = (
            aws_sdk_quicksight.types.table_pinned_field_options.serialize_json(
                value["pinned_field_options"]
            )
        )
    if "transposed_table_options" in value:
        import aws_sdk_quicksight.types.transposed_table_option_list

        out["TransposedTableOptions"] = (
            aws_sdk_quicksight.types.transposed_table_option_list.serialize_json(
                value["transposed_table_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableFieldOptions:
    out: TableFieldOptions = {}  # type: ignore[typeddict-item]
    if "SelectedFieldOptions" in data:
        import aws_sdk_quicksight.types.table_field_option_list

        out["selected_field_options"] = (
            aws_sdk_quicksight.types.table_field_option_list.deserialize_json(
                data["SelectedFieldOptions"]
            )
        )
    if "Order" in data:
        import aws_sdk_quicksight.types.field_order_list

        out["order"] = aws_sdk_quicksight.types.field_order_list.deserialize_json(
            data["Order"]
        )
    if "PinnedFieldOptions" in data:
        import aws_sdk_quicksight.types.table_pinned_field_options

        out["pinned_field_options"] = (
            aws_sdk_quicksight.types.table_pinned_field_options.deserialize_json(
                data["PinnedFieldOptions"]
            )
        )
    if "TransposedTableOptions" in data:
        import aws_sdk_quicksight.types.transposed_table_option_list

        out["transposed_table_options"] = (
            aws_sdk_quicksight.types.transposed_table_option_list.deserialize_json(
                data["TransposedTableOptions"]
            )
        )
    return out
