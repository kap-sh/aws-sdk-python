"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxDataviewsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.max_results
    import aws_sdk_finspace.types.pagination_token


class ListKxDataviewsRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment, for which you want to retrieve a list of dataviews.</p>"""
    database_name: "aws_sdk_finspace.types.database_name.DatabaseName"
    """<p> The name of the database where the dataviews were created.</p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p> A token that indicates where a results page should begin. </p>"""
    max_results: "aws_sdk_finspace.types.max_results.MaxResults"
    """<p>The maximum number of results to return in this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxDataviewsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKxDataviewsRequest:
    out: ListKxDataviewsRequest = {}  # type: ignore[typeddict-item]
    return out
