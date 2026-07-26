"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ExecuteQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.column_descriptions
    import capo_iottwinmaker.types.next_token
    import capo_iottwinmaker.types.rows


class ExecuteQueryResponse(TypedDict, closed=True):
    column_descriptions: NotRequired[
        "capo_iottwinmaker.types.column_descriptions.ColumnDescriptions"
    ]
    """<p>A list of ColumnDescription objects.</p>"""
    rows: NotRequired["capo_iottwinmaker.types.rows.Rows"]
    """<p>Represents a single row in the query results.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteQueryResponse) -> dict:
    out: dict = {}
    if "column_descriptions" in value:
        import capo_iottwinmaker.types.column_descriptions

        out["columnDescriptions"] = (
            capo_iottwinmaker.types.column_descriptions.serialize_json(
                value["column_descriptions"]
            )
        )
    if "rows" in value:
        import capo_iottwinmaker.types.rows

        out["rows"] = capo_iottwinmaker.types.rows.serialize_json(value["rows"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ExecuteQueryResponse:
    out: ExecuteQueryResponse = {}  # type: ignore[typeddict-item]
    if "columnDescriptions" in data:
        import capo_iottwinmaker.types.column_descriptions

        out["column_descriptions"] = (
            capo_iottwinmaker.types.column_descriptions.deserialize_json(
                data["columnDescriptions"]
            )
        )
    if "rows" in data:
        import capo_iottwinmaker.types.rows

        out["rows"] = capo_iottwinmaker.types.rows.deserialize_json(data["rows"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
