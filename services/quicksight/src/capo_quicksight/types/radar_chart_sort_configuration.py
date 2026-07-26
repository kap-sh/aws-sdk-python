"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_sort_options_list
    import capo_quicksight.types.items_limit_configuration


class RadarChartSortConfiguration(TypedDict, closed=True):
    category_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The category sort options of a radar chart.</p>"""
    category_items_limit: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The category items limit for a radar chart.</p>"""
    color_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The color sort configuration of a radar chart.</p>"""
    color_items_limit: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The color items limit of a radar chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartSortConfiguration) -> dict:
    out: dict = {}
    if "category_sort" in value:
        import capo_quicksight.types.field_sort_options_list

        out["CategorySort"] = (
            capo_quicksight.types.field_sort_options_list.serialize_json(
                value["category_sort"]
            )
        )
    if "category_items_limit" in value:
        import capo_quicksight.types.items_limit_configuration

        out["CategoryItemsLimit"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["category_items_limit"]
            )
        )
    if "color_sort" in value:
        import capo_quicksight.types.field_sort_options_list

        out["ColorSort"] = capo_quicksight.types.field_sort_options_list.serialize_json(
            value["color_sort"]
        )
    if "color_items_limit" in value:
        import capo_quicksight.types.items_limit_configuration

        out["ColorItemsLimit"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["color_items_limit"]
            )
        )
    return out


def deserialize_json(data: dict) -> RadarChartSortConfiguration:
    out: RadarChartSortConfiguration = {}  # type: ignore[typeddict-item]
    if "CategorySort" in data:
        import capo_quicksight.types.field_sort_options_list

        out["category_sort"] = (
            capo_quicksight.types.field_sort_options_list.deserialize_json(
                data["CategorySort"]
            )
        )
    if "CategoryItemsLimit" in data:
        import capo_quicksight.types.items_limit_configuration

        out["category_items_limit"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["CategoryItemsLimit"]
            )
        )
    if "ColorSort" in data:
        import capo_quicksight.types.field_sort_options_list

        out["color_sort"] = (
            capo_quicksight.types.field_sort_options_list.deserialize_json(
                data["ColorSort"]
            )
        )
    if "ColorItemsLimit" in data:
        import capo_quicksight.types.items_limit_configuration

        out["color_items_limit"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["ColorItemsLimit"]
            )
        )
    return out
