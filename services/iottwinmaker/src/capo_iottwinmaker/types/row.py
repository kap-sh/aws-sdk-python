"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Row``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.row_data


class Row(TypedDict, closed=True):
    row_data: NotRequired["capo_iottwinmaker.types.row_data.RowData"]
    """<p>The data in a row of query results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Row) -> dict:
    out: dict = {}
    if "row_data" in value:
        import capo_iottwinmaker.types.row_data

        out["rowData"] = capo_iottwinmaker.types.row_data.serialize_json(
            value["row_data"]
        )
    return out


def deserialize_json(data: dict) -> Row:
    out: Row = {}  # type: ignore[typeddict-item]
    if "rowData" in data:
        import capo_iottwinmaker.types.row_data

        out["row_data"] = capo_iottwinmaker.types.row_data.deserialize_json(
            data["rowData"]
        )
    return out
