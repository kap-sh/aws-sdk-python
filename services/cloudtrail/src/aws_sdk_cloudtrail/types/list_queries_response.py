"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListQueriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.pagination_token
    import aws_sdk_cloudtrail.types.queries


class ListQueriesResponse(TypedDict):
    queries: NotRequired["aws_sdk_cloudtrail.types.queries.Queries"]
    """<p>Lists matching query results, and shows query ID, status, and creation time of each query.</p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>A token you can use to get the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQueriesResponse) -> dict:
    out: dict = {}
    if "queries" in value:
        import aws_sdk_cloudtrail.types.queries

        out["Queries"] = aws_sdk_cloudtrail.types.queries.serialize_aws_json_1_1(
            value["queries"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQueriesResponse:
    out: ListQueriesResponse = {}  # type: ignore[typeddict-item]
    if "Queries" in data:
        import aws_sdk_cloudtrail.types.queries

        out["queries"] = aws_sdk_cloudtrail.types.queries.deserialize_aws_json_1_1(
            data["Queries"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
