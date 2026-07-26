"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_sort_options_list
    import capo_quicksight.types.items_limit_configuration


class LineChartSortConfiguration(TypedDict, closed=True):
    category_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the category fields.</p>"""
    category_items_limit_configuration: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of categories that are displayed in a line chart.</p>"""
    color_items_limit_configuration: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of lines that are displayed in a line chart.</p>"""
    small_multiples_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the small multiples field.</p>"""
    small_multiples_limit_configuration: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of small multiples panels that are displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineChartSortConfiguration) -> dict:
    out: dict = {}
    if "category_sort" in value:
        import capo_quicksight.types.field_sort_options_list

        out["CategorySort"] = (
            capo_quicksight.types.field_sort_options_list.serialize_json(
                value["category_sort"]
            )
        )
    if "category_items_limit_configuration" in value:
        import capo_quicksight.types.items_limit_configuration

        out["CategoryItemsLimitConfiguration"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["category_items_limit_configuration"]
            )
        )
    if "color_items_limit_configuration" in value:
        import capo_quicksight.types.items_limit_configuration

        out["ColorItemsLimitConfiguration"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["color_items_limit_configuration"]
            )
        )
    if "small_multiples_sort" in value:
        import capo_quicksight.types.field_sort_options_list

        out["SmallMultiplesSort"] = (
            capo_quicksight.types.field_sort_options_list.serialize_json(
                value["small_multiples_sort"]
            )
        )
    if "small_multiples_limit_configuration" in value:
        import capo_quicksight.types.items_limit_configuration

        out["SmallMultiplesLimitConfiguration"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["small_multiples_limit_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineChartSortConfiguration:
    out: LineChartSortConfiguration = {}  # type: ignore[typeddict-item]
    if "CategorySort" in data:
        import capo_quicksight.types.field_sort_options_list

        out["category_sort"] = (
            capo_quicksight.types.field_sort_options_list.deserialize_json(
                data["CategorySort"]
            )
        )
    if "CategoryItemsLimitConfiguration" in data:
        import capo_quicksight.types.items_limit_configuration

        out["category_items_limit_configuration"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["CategoryItemsLimitConfiguration"]
            )
        )
    if "ColorItemsLimitConfiguration" in data:
        import capo_quicksight.types.items_limit_configuration

        out["color_items_limit_configuration"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["ColorItemsLimitConfiguration"]
            )
        )
    if "SmallMultiplesSort" in data:
        import capo_quicksight.types.field_sort_options_list

        out["small_multiples_sort"] = (
            capo_quicksight.types.field_sort_options_list.deserialize_json(
                data["SmallMultiplesSort"]
            )
        )
    if "SmallMultiplesLimitConfiguration" in data:
        import capo_quicksight.types.items_limit_configuration

        out["small_multiples_limit_configuration"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["SmallMultiplesLimitConfiguration"]
            )
        )
    return out
