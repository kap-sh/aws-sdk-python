"""Generated from Smithy shape ``com.amazonaws.quicksight#TableSortConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pagination_configuration
    import aws_sdk_quicksight.types.row_sort_list


class TableSortConfiguration(TypedDict):
    row_sort: NotRequired["aws_sdk_quicksight.types.row_sort_list.RowSortList"]
    """<p>The field sort options for rows in the table.</p>"""
    pagination_configuration: NotRequired[
        "aws_sdk_quicksight.types.pagination_configuration.PaginationConfiguration"
    ]
    """<p>The pagination configuration (page size, page number) for the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableSortConfiguration) -> dict:
    out: dict = {}
    if "row_sort" in value:
        import aws_sdk_quicksight.types.row_sort_list

        out["RowSort"] = aws_sdk_quicksight.types.row_sort_list.serialize_json(
            value["row_sort"]
        )
    if "pagination_configuration" in value:
        import aws_sdk_quicksight.types.pagination_configuration

        out["PaginationConfiguration"] = (
            aws_sdk_quicksight.types.pagination_configuration.serialize_json(
                value["pagination_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableSortConfiguration:
    out: TableSortConfiguration = {}  # type: ignore[typeddict-item]
    if "RowSort" in data:
        import aws_sdk_quicksight.types.row_sort_list

        out["row_sort"] = aws_sdk_quicksight.types.row_sort_list.deserialize_json(
            data["RowSort"]
        )
    if "PaginationConfiguration" in data:
        import aws_sdk_quicksight.types.pagination_configuration

        out["pagination_configuration"] = (
            aws_sdk_quicksight.types.pagination_configuration.deserialize_json(
                data["PaginationConfiguration"]
            )
        )
    return out
