"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListStateTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.next_token


class ListStateTemplatesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""
    max_results: NotRequired["capo_iotfleetwise.types.max_results.maxResults"]
    """<p>The maximum number of items to return, between 1 and 100, inclusive.</p>"""
    list_response_scope: NotRequired[
        "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
    ]
    """<p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: state template ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListStateTemplatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListStateTemplatesRequest:
    out: ListStateTemplatesRequest = {}  # type: ignore[typeddict-item]
    return out
