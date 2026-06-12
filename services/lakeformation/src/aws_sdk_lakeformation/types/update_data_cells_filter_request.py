"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateDataCellsFilterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.data_cells_filter


class UpdateDataCellsFilterRequest(TypedDict):
    table_data: "aws_sdk_lakeformation.types.data_cells_filter.DataCellsFilter"
    """<p>A <code>DataCellsFilter</code> structure containing information about the data cells filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataCellsFilterRequest) -> dict:
    out: dict = {}
    import aws_sdk_lakeformation.types.data_cells_filter

    out["TableData"] = aws_sdk_lakeformation.types.data_cells_filter.serialize_json(
        value["table_data"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataCellsFilterRequest:
    out: UpdateDataCellsFilterRequest = {}  # type: ignore[typeddict-item]
    if "TableData" in data:
        import aws_sdk_lakeformation.types.data_cells_filter

        out["table_data"] = (
            aws_sdk_lakeformation.types.data_cells_filter.deserialize_json(
                data["TableData"]
            )
        )
    else:
        raise DeserializationError("UpdateDataCellsFilterRequest.table_data required")
    return out
