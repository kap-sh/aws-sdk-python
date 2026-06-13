"""Generated from Smithy shape ``com.amazonaws.quicksight#RowInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.long


class RowInfo(TypedDict):
    rows_ingested: NotRequired["aws_sdk_quicksight.types.long.Long"]
    """<p>The number of rows that were ingested.</p>"""
    rows_dropped: NotRequired["aws_sdk_quicksight.types.long.Long"]
    """<p>The number of rows that were not ingested.</p>"""
    total_rows_in_dataset: NotRequired["aws_sdk_quicksight.types.long.Long"]
    """<p>The total number of rows in the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RowInfo) -> dict:
    out: dict = {}
    if "rows_ingested" in value:
        out["RowsIngested"] = value["rows_ingested"]
    if "rows_dropped" in value:
        out["RowsDropped"] = value["rows_dropped"]
    if "total_rows_in_dataset" in value:
        out["TotalRowsInDataset"] = value["total_rows_in_dataset"]
    return out


def deserialize_json(data: dict) -> RowInfo:
    out: RowInfo = {}  # type: ignore[typeddict-item]
    if "RowsIngested" in data:
        out["rows_ingested"] = data["RowsIngested"]
    if "RowsDropped" in data:
        out["rows_dropped"] = data["RowsDropped"]
    if "TotalRowsInDataset" in data:
        out["total_rows_in_dataset"] = data["TotalRowsInDataset"]
    return out
