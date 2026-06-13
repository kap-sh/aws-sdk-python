"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartSortConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_sort_options_list
    import aws_sdk_quicksight.types.items_limit_configuration


class BarChartSortConfiguration(TypedDict):
    category_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of category fields.</p>"""
    category_items_limit: NotRequired[
        "aws_sdk_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of categories displayed in a bar chart.</p>"""
    color_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of color fields in a bar chart.</p>"""
    color_items_limit: NotRequired[
        "aws_sdk_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of values displayed in a bar chart.</p>"""
    small_multiples_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the small multiples field.</p>"""
    small_multiples_limit_configuration: NotRequired[
        "aws_sdk_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of small multiples panels that are displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarChartSortConfiguration) -> dict:
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
    if "small_multiples_sort" in value:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["SmallMultiplesSort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.serialize_json(
                value["small_multiples_sort"]
            )
        )
    if "small_multiples_limit_configuration" in value:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["SmallMultiplesLimitConfiguration"] = (
            aws_sdk_quicksight.types.items_limit_configuration.serialize_json(
                value["small_multiples_limit_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BarChartSortConfiguration:
    out: BarChartSortConfiguration = {}  # type: ignore[typeddict-item]
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
    if "SmallMultiplesSort" in data:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["small_multiples_sort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.deserialize_json(
                data["SmallMultiplesSort"]
            )
        )
    if "SmallMultiplesLimitConfiguration" in data:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["small_multiples_limit_configuration"] = (
            aws_sdk_quicksight.types.items_limit_configuration.deserialize_json(
                data["SmallMultiplesLimitConfiguration"]
            )
        )
    return out
