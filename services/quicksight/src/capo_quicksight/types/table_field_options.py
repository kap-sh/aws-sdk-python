"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_order_list
    import capo_quicksight.types.table_field_option_list
    import capo_quicksight.types.table_pinned_field_options
    import capo_quicksight.types.transposed_table_option_list


class TableFieldOptions(TypedDict, closed=True):
    selected_field_options: NotRequired[
        "capo_quicksight.types.table_field_option_list.TableFieldOptionList"
    ]
    """<p>The field options to be configured to a table.</p>"""
    order: NotRequired["capo_quicksight.types.field_order_list.FieldOrderList"]
    """<p>The order of the field IDs that are configured as field options for a table visual.</p>"""
    pinned_field_options: NotRequired[
        "capo_quicksight.types.table_pinned_field_options.TablePinnedFieldOptions"
    ]
    """<p>The settings for the pinned columns of a table visual.</p>"""
    transposed_table_options: NotRequired[
        "capo_quicksight.types.transposed_table_option_list.TransposedTableOptionList"
    ]
    """<p>The <code>TableOptions</code> of a transposed table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldOptions) -> dict:
    out: dict = {}
    if "selected_field_options" in value:
        import capo_quicksight.types.table_field_option_list

        out["SelectedFieldOptions"] = (
            capo_quicksight.types.table_field_option_list.serialize_json(
                value["selected_field_options"]
            )
        )
    if "order" in value:
        import capo_quicksight.types.field_order_list

        out["Order"] = capo_quicksight.types.field_order_list.serialize_json(
            value["order"]
        )
    if "pinned_field_options" in value:
        import capo_quicksight.types.table_pinned_field_options

        out["PinnedFieldOptions"] = (
            capo_quicksight.types.table_pinned_field_options.serialize_json(
                value["pinned_field_options"]
            )
        )
    if "transposed_table_options" in value:
        import capo_quicksight.types.transposed_table_option_list

        out["TransposedTableOptions"] = (
            capo_quicksight.types.transposed_table_option_list.serialize_json(
                value["transposed_table_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableFieldOptions:
    out: TableFieldOptions = {}  # type: ignore[typeddict-item]
    if "SelectedFieldOptions" in data:
        import capo_quicksight.types.table_field_option_list

        out["selected_field_options"] = (
            capo_quicksight.types.table_field_option_list.deserialize_json(
                data["SelectedFieldOptions"]
            )
        )
    if "Order" in data:
        import capo_quicksight.types.field_order_list

        out["order"] = capo_quicksight.types.field_order_list.deserialize_json(
            data["Order"]
        )
    if "PinnedFieldOptions" in data:
        import capo_quicksight.types.table_pinned_field_options

        out["pinned_field_options"] = (
            capo_quicksight.types.table_pinned_field_options.deserialize_json(
                data["PinnedFieldOptions"]
            )
        )
    if "TransposedTableOptions" in data:
        import capo_quicksight.types.transposed_table_option_list

        out["transposed_table_options"] = (
            capo_quicksight.types.transposed_table_option_list.deserialize_json(
                data["TransposedTableOptions"]
            )
        )
    return out
