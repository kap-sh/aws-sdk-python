"""Generated from Smithy shape ``com.amazonaws.quicksight#TreeMapSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_sort_options_list
    import aws_sdk_quicksight.types.items_limit_configuration


class TreeMapSortConfiguration(TypedDict, closed=True):
    tree_map_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of group by fields.</p>"""
    tree_map_group_items_limit_configuration: NotRequired[
        "aws_sdk_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of groups that are displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TreeMapSortConfiguration) -> dict:
    out: dict = {}
    if "tree_map_sort" in value:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["TreeMapSort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.serialize_json(
                value["tree_map_sort"]
            )
        )
    if "tree_map_group_items_limit_configuration" in value:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["TreeMapGroupItemsLimitConfiguration"] = (
            aws_sdk_quicksight.types.items_limit_configuration.serialize_json(
                value["tree_map_group_items_limit_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TreeMapSortConfiguration:
    out: TreeMapSortConfiguration = {}  # type: ignore[typeddict-item]
    if "TreeMapSort" in data:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["tree_map_sort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.deserialize_json(
                data["TreeMapSort"]
            )
        )
    if "TreeMapGroupItemsLimitConfiguration" in data:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["tree_map_group_items_limit_configuration"] = (
            aws_sdk_quicksight.types.items_limit_configuration.deserialize_json(
                data["TreeMapGroupItemsLimitConfiguration"]
            )
        )
    return out
