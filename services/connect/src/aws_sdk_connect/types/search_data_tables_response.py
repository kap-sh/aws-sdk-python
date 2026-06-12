"""Generated from Smithy shape ``com.amazonaws.connect#SearchDataTablesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.data_table_list
    import aws_sdk_connect.types.next_token


class SearchDataTablesResponse(TypedDict):
    data_tables: NotRequired["aws_sdk_connect.types.data_table_list.DataTableList"]
    """<p>An array of data tables matching the search criteria with the same structure as DescribeTable except Version, VersionDescription, and LockVersion are omitted.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The approximate number of data tables that matched the search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDataTablesResponse) -> dict:
    out: dict = {}
    if "data_tables" in value:
        import aws_sdk_connect.types.data_table_list

        out["DataTables"] = aws_sdk_connect.types.data_table_list.serialize_json(
            value["data_tables"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchDataTablesResponse:
    out: SearchDataTablesResponse = {}  # type: ignore[typeddict-item]
    if "DataTables" in data:
        import aws_sdk_connect.types.data_table_list

        out["data_tables"] = aws_sdk_connect.types.data_table_list.deserialize_json(
            data["DataTables"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
