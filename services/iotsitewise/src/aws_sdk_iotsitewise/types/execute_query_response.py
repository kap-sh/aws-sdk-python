"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecuteQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.columns_list
    import aws_sdk_iotsitewise.types.execute_query_next_token
    import aws_sdk_iotsitewise.types.rows


class ExecuteQueryResponse(TypedDict, closed=True):
    columns: NotRequired["aws_sdk_iotsitewise.types.columns_list.ColumnsList"]
    """<p>Represents a single column in the query results.</p>"""
    rows: NotRequired["aws_sdk_iotsitewise.types.rows.Rows"]
    """<p>Represents a single row in the query results.</p>"""
    next_token: NotRequired[
        "aws_sdk_iotsitewise.types.execute_query_next_token.ExecuteQueryNextToken"
    ]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteQueryResponse) -> dict:
    out: dict = {}
    if "columns" in value:
        import aws_sdk_iotsitewise.types.columns_list

        out["columns"] = aws_sdk_iotsitewise.types.columns_list.serialize_json(
            value["columns"]
        )
    if "rows" in value:
        import aws_sdk_iotsitewise.types.rows

        out["rows"] = aws_sdk_iotsitewise.types.rows.serialize_json(value["rows"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ExecuteQueryResponse:
    out: ExecuteQueryResponse = {}  # type: ignore[typeddict-item]
    if "columns" in data:
        import aws_sdk_iotsitewise.types.columns_list

        out["columns"] = aws_sdk_iotsitewise.types.columns_list.deserialize_json(
            data["columns"]
        )
    if "rows" in data:
        import aws_sdk_iotsitewise.types.rows

        out["rows"] = aws_sdk_iotsitewise.types.rows.deserialize_json(data["rows"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
