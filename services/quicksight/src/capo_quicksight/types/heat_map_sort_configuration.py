"""Generated from Smithy shape ``com.amazonaws.quicksight#HeatMapSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_sort_options_list
    import capo_quicksight.types.items_limit_configuration


class HeatMapSortConfiguration(TypedDict, closed=True):
    heat_map_row_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The field sort configuration of the rows fields.</p>"""
    heat_map_column_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The column sort configuration for heat map for columns that aren't a part of a field well.</p>"""
    heat_map_row_items_limit_configuration: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of rows that are displayed in a heat map.</p>"""
    heat_map_column_items_limit_configuration: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of columns that are displayed in a heat map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeatMapSortConfiguration) -> dict:
    out: dict = {}
    if "heat_map_row_sort" in value:
        import capo_quicksight.types.field_sort_options_list

        out["HeatMapRowSort"] = (
            capo_quicksight.types.field_sort_options_list.serialize_json(
                value["heat_map_row_sort"]
            )
        )
    if "heat_map_column_sort" in value:
        import capo_quicksight.types.field_sort_options_list

        out["HeatMapColumnSort"] = (
            capo_quicksight.types.field_sort_options_list.serialize_json(
                value["heat_map_column_sort"]
            )
        )
    if "heat_map_row_items_limit_configuration" in value:
        import capo_quicksight.types.items_limit_configuration

        out["HeatMapRowItemsLimitConfiguration"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["heat_map_row_items_limit_configuration"]
            )
        )
    if "heat_map_column_items_limit_configuration" in value:
        import capo_quicksight.types.items_limit_configuration

        out["HeatMapColumnItemsLimitConfiguration"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["heat_map_column_items_limit_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> HeatMapSortConfiguration:
    out: HeatMapSortConfiguration = {}  # type: ignore[typeddict-item]
    if "HeatMapRowSort" in data:
        import capo_quicksight.types.field_sort_options_list

        out["heat_map_row_sort"] = (
            capo_quicksight.types.field_sort_options_list.deserialize_json(
                data["HeatMapRowSort"]
            )
        )
    if "HeatMapColumnSort" in data:
        import capo_quicksight.types.field_sort_options_list

        out["heat_map_column_sort"] = (
            capo_quicksight.types.field_sort_options_list.deserialize_json(
                data["HeatMapColumnSort"]
            )
        )
    if "HeatMapRowItemsLimitConfiguration" in data:
        import capo_quicksight.types.items_limit_configuration

        out["heat_map_row_items_limit_configuration"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["HeatMapRowItemsLimitConfiguration"]
            )
        )
    if "HeatMapColumnItemsLimitConfiguration" in data:
        import capo_quicksight.types.items_limit_configuration

        out["heat_map_column_items_limit_configuration"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["HeatMapColumnItemsLimitConfiguration"]
            )
        )
    return out
