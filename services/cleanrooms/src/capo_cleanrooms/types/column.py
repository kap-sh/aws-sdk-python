"""Generated from Smithy shape ``com.amazonaws.cleanrooms#Column``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.column_name
    import capo_cleanrooms.types.column_type_string


class Column(TypedDict, closed=True):
    name: "capo_cleanrooms.types.column_name.ColumnName"
    """<p>The name of the column.</p>"""
    type: "capo_cleanrooms.types.column_type_string.ColumnTypeString"
    """<p>The type of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Column) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Column:
    out: Column = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Column.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Column.type required")
    return out
