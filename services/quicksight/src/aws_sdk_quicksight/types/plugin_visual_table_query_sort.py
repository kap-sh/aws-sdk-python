"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualTableQuerySort``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.plugin_visual_items_limit_configuration
    import aws_sdk_quicksight.types.row_sort_list


class PluginVisualTableQuerySort(TypedDict):
    row_sort: NotRequired["aws_sdk_quicksight.types.row_sort_list.RowSortList"]
    """<p>Determines how data is sorted in the response.</p>"""
    items_limit_configuration: NotRequired[
        "aws_sdk_quicksight.types.plugin_visual_items_limit_configuration.PluginVisualItemsLimitConfiguration"
    ]
    """<p>The maximum amount of data to be returned by a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualTableQuerySort) -> dict:
    out: dict = {}
    if "row_sort" in value:
        import aws_sdk_quicksight.types.row_sort_list

        out["RowSort"] = aws_sdk_quicksight.types.row_sort_list.serialize_json(
            value["row_sort"]
        )
    if "items_limit_configuration" in value:
        import aws_sdk_quicksight.types.plugin_visual_items_limit_configuration

        out["ItemsLimitConfiguration"] = (
            aws_sdk_quicksight.types.plugin_visual_items_limit_configuration.serialize_json(
                value["items_limit_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PluginVisualTableQuerySort:
    out: PluginVisualTableQuerySort = {}  # type: ignore[typeddict-item]
    if "RowSort" in data:
        import aws_sdk_quicksight.types.row_sort_list

        out["row_sort"] = aws_sdk_quicksight.types.row_sort_list.deserialize_json(
            data["RowSort"]
        )
    if "ItemsLimitConfiguration" in data:
        import aws_sdk_quicksight.types.plugin_visual_items_limit_configuration

        out["items_limit_configuration"] = (
            aws_sdk_quicksight.types.plugin_visual_items_limit_configuration.deserialize_json(
                data["ItemsLimitConfiguration"]
            )
        )
    return out
