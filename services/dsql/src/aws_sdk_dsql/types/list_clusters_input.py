"""Generated from Smithy shape ``com.amazonaws.dsql#ListClustersInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_dsql.types.max_results
    import aws_sdk_dsql.types.next_token

class ListClustersInput(TypedDict):
    max_results: "aws_sdk_dsql.types.max_results.MaxResults"
    """<p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>"""
    next_token: NotRequired["aws_sdk_dsql.types.next_token.NextToken"]
    """<p>If your initial ListClusters operation returns a nextToken, you can include the returned nextToken in following ListClusters operations, which returns results in the next page.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListClustersInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClustersInput:
    out: ListClustersInput = {}  # type: ignore[typeddict-item]
    return out