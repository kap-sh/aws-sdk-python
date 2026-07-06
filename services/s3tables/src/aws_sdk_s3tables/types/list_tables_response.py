"""Generated from Smithy shape ``com.amazonaws.s3tables#ListTablesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.next_token
    import aws_sdk_s3tables.types.table_summary_list


class ListTablesResponse(TypedDict, closed=True):
    tables: "aws_sdk_s3tables.types.table_summary_list.TableSummaryList"
    """<p>A list of tables.</p>"""
    continuation_token: NotRequired["aws_sdk_s3tables.types.next_token.NextToken"]
    """<p>You can use this <code>ContinuationToken</code> for pagination of the list results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTablesResponse) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.table_summary_list

    out["tables"] = aws_sdk_s3tables.types.table_summary_list.serialize_json(
        value["tables"]
    )
    if "continuation_token" in value:
        out["continuationToken"] = value["continuation_token"]
    return out


def deserialize_json(data: dict) -> ListTablesResponse:
    out: ListTablesResponse = {}  # type: ignore[typeddict-item]
    if "tables" in data:
        import aws_sdk_s3tables.types.table_summary_list

        out["tables"] = aws_sdk_s3tables.types.table_summary_list.deserialize_json(
            data["tables"]
        )
    else:
        raise DeserializationError("ListTablesResponse.tables required")
    if "continuationToken" in data:
        out["continuation_token"] = data["continuationToken"]
    return out
