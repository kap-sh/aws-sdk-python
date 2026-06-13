"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListProtectedQueriesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.protected_query_summary_list


class ListProtectedQueriesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    protected_queries: "aws_sdk_cleanrooms.types.protected_query_summary_list.ProtectedQuerySummaryList"
    """<p>A list of protected queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProtectedQueriesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanrooms.types.protected_query_summary_list

    out["protectedQueries"] = (
        aws_sdk_cleanrooms.types.protected_query_summary_list.serialize_json(
            value["protected_queries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListProtectedQueriesOutput:
    out: ListProtectedQueriesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "protectedQueries" in data:
        import aws_sdk_cleanrooms.types.protected_query_summary_list

        out["protected_queries"] = (
            aws_sdk_cleanrooms.types.protected_query_summary_list.deserialize_json(
                data["protectedQueries"]
            )
        )
    else:
        raise DeserializationError(
            "ListProtectedQueriesOutput.protected_queries required"
        )
    return out
