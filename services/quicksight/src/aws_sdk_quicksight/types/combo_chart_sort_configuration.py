"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboChartSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_sort_options_list
    import aws_sdk_quicksight.types.items_limit_configuration


class ComboChartSortConfiguration(TypedDict, closed=True):
    category_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the category field well in a combo chart.</p>"""
    category_items_limit: NotRequired[
        "aws_sdk_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The item limit configuration for the category field well of a combo chart.</p>"""
    color_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the color field well in a combo chart.</p>"""
    color_items_limit: NotRequired[
        "aws_sdk_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The item limit configuration of the color field well in a combo chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComboChartSortConfiguration) -> dict:
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
    if "color_sort" in value:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["ColorSort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.serialize_json(
                value["color_sort"]
            )
        )
    if "color_items_limit" in value:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["ColorItemsLimit"] = (
            aws_sdk_quicksight.types.items_limit_configuration.serialize_json(
                value["color_items_limit"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComboChartSortConfiguration:
    out: ComboChartSortConfiguration = {}  # type: ignore[typeddict-item]
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
    if "ColorSort" in data:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["color_sort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.deserialize_json(
                data["ColorSort"]
            )
        )
    if "ColorItemsLimit" in data:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["color_items_limit"] = (
            aws_sdk_quicksight.types.items_limit_configuration.deserialize_json(
                data["ColorItemsLimit"]
            )
        )
    return out
