"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_sort_options_list
    import capo_quicksight.types.items_limit_configuration


class WaterfallChartSortConfiguration(TypedDict, closed=True):
    category_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the category fields.</p>"""
    breakdown_items_limit: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of bar groups that are displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaterfallChartSortConfiguration) -> dict:
    out: dict = {}
    if "category_sort" in value:
        import capo_quicksight.types.field_sort_options_list

        out["CategorySort"] = (
            capo_quicksight.types.field_sort_options_list.serialize_json(
                value["category_sort"]
            )
        )
    if "breakdown_items_limit" in value:
        import capo_quicksight.types.items_limit_configuration

        out["BreakdownItemsLimit"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["breakdown_items_limit"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaterfallChartSortConfiguration:
    out: WaterfallChartSortConfiguration = {}  # type: ignore[typeddict-item]
    if "CategorySort" in data:
        import capo_quicksight.types.field_sort_options_list

        out["category_sort"] = (
            capo_quicksight.types.field_sort_options_list.deserialize_json(
                data["CategorySort"]
            )
        )
    if "BreakdownItemsLimit" in data:
        import capo_quicksight.types.items_limit_configuration

        out["breakdown_items_limit"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["BreakdownItemsLimit"]
            )
        )
    return out
