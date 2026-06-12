"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListDataCellsFilterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.data_cells_filter_list
    import aws_sdk_lakeformation.types.token


class ListDataCellsFilterResponse(TypedDict):
    data_cells_filters: NotRequired[
        "aws_sdk_lakeformation.types.data_cells_filter_list.DataCellsFilterList"
    ]
    """<p>A list of <code>DataCellFilter</code> structures.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, if not all requested data cell filters have been returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataCellsFilterResponse) -> dict:
    out: dict = {}
    if "data_cells_filters" in value:
        import aws_sdk_lakeformation.types.data_cells_filter_list

        out["DataCellsFilters"] = (
            aws_sdk_lakeformation.types.data_cells_filter_list.serialize_json(
                value["data_cells_filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataCellsFilterResponse:
    out: ListDataCellsFilterResponse = {}  # type: ignore[typeddict-item]
    if "DataCellsFilters" in data:
        import aws_sdk_lakeformation.types.data_cells_filter_list

        out["data_cells_filters"] = (
            aws_sdk_lakeformation.types.data_cells_filter_list.deserialize_json(
                data["DataCellsFilters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
