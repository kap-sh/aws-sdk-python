"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_sort_options_list
    import aws_sdk_quicksight.types.pagination_configuration


class BoxPlotSortConfiguration(TypedDict, closed=True):
    category_sort: NotRequired[
        "aws_sdk_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of a group by fields.</p>"""
    pagination_configuration: NotRequired[
        "aws_sdk_quicksight.types.pagination_configuration.PaginationConfiguration"
    ]
    """<p>The pagination configuration of a table visual or box plot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotSortConfiguration) -> dict:
    out: dict = {}
    if "category_sort" in value:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["CategorySort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.serialize_json(
                value["category_sort"]
            )
        )
    if "pagination_configuration" in value:
        import aws_sdk_quicksight.types.pagination_configuration

        out["PaginationConfiguration"] = (
            aws_sdk_quicksight.types.pagination_configuration.serialize_json(
                value["pagination_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BoxPlotSortConfiguration:
    out: BoxPlotSortConfiguration = {}  # type: ignore[typeddict-item]
    if "CategorySort" in data:
        import aws_sdk_quicksight.types.field_sort_options_list

        out["category_sort"] = (
            aws_sdk_quicksight.types.field_sort_options_list.deserialize_json(
                data["CategorySort"]
            )
        )
    if "PaginationConfiguration" in data:
        import aws_sdk_quicksight.types.pagination_configuration

        out["pagination_configuration"] = (
            aws_sdk_quicksight.types.pagination_configuration.deserialize_json(
                data["PaginationConfiguration"]
            )
        )
    return out
