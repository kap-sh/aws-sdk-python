"""Generated from Smithy shape ``com.amazonaws.lakeformation#CreateDataCellsFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.data_cells_filter


class CreateDataCellsFilterRequest(TypedDict, closed=True):
    table_data: "aws_sdk_lakeformation.types.data_cells_filter.DataCellsFilter"
    """<p>A <code>DataCellsFilter</code> structure containing information about the data cells filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataCellsFilterRequest) -> dict:
    out: dict = {}
    import aws_sdk_lakeformation.types.data_cells_filter

    out["TableData"] = aws_sdk_lakeformation.types.data_cells_filter.serialize_json(
        value["table_data"]
    )
    return out


def deserialize_json(data: dict) -> CreateDataCellsFilterRequest:
    out: CreateDataCellsFilterRequest = {}  # type: ignore[typeddict-item]
    if "TableData" in data:
        import aws_sdk_lakeformation.types.data_cells_filter

        out["table_data"] = (
            aws_sdk_lakeformation.types.data_cells_filter.deserialize_json(
                data["TableData"]
            )
        )
    else:
        raise DeserializationError("CreateDataCellsFilterRequest.table_data required")
    return out
