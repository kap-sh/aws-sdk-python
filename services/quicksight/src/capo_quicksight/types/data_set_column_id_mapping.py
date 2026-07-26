"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetColumnIdMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_id


class DataSetColumnIdMapping(TypedDict, closed=True):
    source_column_id: "capo_quicksight.types.column_id.ColumnId"
    """<p>Source column ID.</p>"""
    target_column_id: "capo_quicksight.types.column_id.ColumnId"
    """<p>Target column ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetColumnIdMapping) -> dict:
    out: dict = {}
    out["SourceColumnId"] = value["source_column_id"]
    out["TargetColumnId"] = value["target_column_id"]
    return out


def deserialize_json(data: dict) -> DataSetColumnIdMapping:
    out: DataSetColumnIdMapping = {}  # type: ignore[typeddict-item]
    if "SourceColumnId" in data:
        out["source_column_id"] = data["SourceColumnId"]
    else:
        raise DeserializationError("DataSetColumnIdMapping.source_column_id required")
    if "TargetColumnId" in data:
        out["target_column_id"] = data["TargetColumnId"]
    else:
        raise DeserializationError("DataSetColumnIdMapping.target_column_id required")
    return out
