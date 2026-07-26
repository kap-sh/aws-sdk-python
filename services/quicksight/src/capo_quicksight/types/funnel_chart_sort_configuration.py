"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_sort_options_list
    import capo_quicksight.types.items_limit_configuration


class FunnelChartSortConfiguration(TypedDict, closed=True):
    category_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the category fields.</p>"""
    category_items_limit: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of categories displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartSortConfiguration) -> dict:
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
    return out


def deserialize_json(data: dict) -> FunnelChartSortConfiguration:
    out: FunnelChartSortConfiguration = {}  # type: ignore[typeddict-item]
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
    return out
