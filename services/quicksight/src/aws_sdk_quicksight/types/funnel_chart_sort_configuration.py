"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_sort_options_list
    import aws_sdk_quicksight.types.items_limit_configuration


class FunnelChartSortConfiguration(TypedDict, closed=True):
    category_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the category fields.</p>"""
    category_items_limit: NotRequired[
        "aws_sdk_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of categories displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartSortConfiguration) -> dict:
    out: dict = {}
    if "category_sort" in value:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["CategorySort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.serialize_json(
                value["category_sort"]
            )
        )
    if "category_items_limit" in value:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["CategoryItemsLimit"] = (
            aws_sdk_quicksight.types.items_limit_configuration.serialize_json(
                value["category_items_limit"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunnelChartSortConfiguration:
    out: FunnelChartSortConfiguration = {}  # type: ignore[typeddict-item]
    if "CategorySort" in data:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["category_sort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.deserialize_json(
                data["CategorySort"]
            )
        )
    if "CategoryItemsLimit" in data:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["category_items_limit"] = (
            aws_sdk_quicksight.types.items_limit_configuration.deserialize_json(
                data["CategoryItemsLimit"]
            )
        )
    return out
