"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxDatabasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.max_results
    import aws_sdk_finspace.types.pagination_token


class ListKxDatabasesRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: "aws_sdk_finspace.types.max_results.MaxResults"
    """<p>The maximum number of results to return in this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxDatabasesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKxDatabasesRequest:
    out: ListKxDatabasesRequest = {}  # type: ignore[typeddict-item]
    return out
