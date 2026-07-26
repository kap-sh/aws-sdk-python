"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListFleetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.next_token


class ListFleetsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>"""
    max_results: NotRequired["capo_iotfleetwise.types.max_results.maxResults"]
    """<p>The maximum number of items to return, between 1 and 100, inclusive.</p>"""
    list_response_scope: NotRequired[
        "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
    ]
    """<p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: fleet ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFleetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFleetsRequest:
    out: ListFleetsRequest = {}  # type: ignore[typeddict-item]
    return out
