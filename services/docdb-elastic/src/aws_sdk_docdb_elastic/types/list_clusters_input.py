"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ListClustersInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.pagination_token


class ListClustersInput(TypedDict):
    next_token: NotRequired[
        "aws_sdk_docdb_elastic.types.pagination_token.PaginationToken"
    ]
    """<p>A pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond this token, up to the value specified by <code>max-results</code>.</p> <p>If there is no more data in the responce, the <code>nextToken</code> will not be returned.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of elastic cluster snapshot results to receive in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClustersInput:
    out: ListClustersInput = {}  # type: ignore[typeddict-item]
    return out
