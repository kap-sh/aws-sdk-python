"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudSortConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_sort_options_list
    import aws_sdk_quicksight.types.items_limit_configuration


class WordCloudSortConfiguration(TypedDict):
    category_items_limit: NotRequired[
        "aws_sdk_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of groups that are displayed in a word cloud.</p>"""
    category_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of group by fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudSortConfiguration) -> dict:
    out: dict = {}
    if "category_items_limit" in value:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["CategoryItemsLimit"] = (
            aws_sdk_quicksight.types.items_limit_configuration.serialize_json(
                value["category_items_limit"]
            )
        )
    if "category_sort" in value:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["CategorySort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.serialize_json(
                value["category_sort"]
            )
        )
    return out


def deserialize_json(data: dict) -> WordCloudSortConfiguration:
    out: WordCloudSortConfiguration = {}  # type: ignore[typeddict-item]
    if "CategoryItemsLimit" in data:
        import aws_sdk_quicksight.types.items_limit_configuration

        out["category_items_limit"] = (
            aws_sdk_quicksight.types.items_limit_configuration.deserialize_json(
                data["CategoryItemsLimit"]
            )
        )
    if "CategorySort" in data:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["category_sort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.deserialize_json(
                data["CategorySort"]
            )
        )
    return out
