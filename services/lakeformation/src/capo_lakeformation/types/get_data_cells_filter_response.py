"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetDataCellsFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.data_cells_filter


class GetDataCellsFilterResponse(TypedDict, closed=True):
    data_cells_filter: NotRequired[
        "capo_lakeformation.types.data_cells_filter.DataCellsFilter"
    ]
    """<p>A structure that describes certain columns on certain rows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataCellsFilterResponse) -> dict:
    out: dict = {}
    if "data_cells_filter" in value:
        import capo_lakeformation.types.data_cells_filter

        out["DataCellsFilter"] = (
            capo_lakeformation.types.data_cells_filter.serialize_json(
                value["data_cells_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataCellsFilterResponse:
    out: GetDataCellsFilterResponse = {}  # type: ignore[typeddict-item]
    if "DataCellsFilter" in data:
        import capo_lakeformation.types.data_cells_filter

        out["data_cells_filter"] = (
            capo_lakeformation.types.data_cells_filter.deserialize_json(
                data["DataCellsFilter"]
            )
        )
    return out
