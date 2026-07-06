"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ListConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.max_results
    import aws_sdk_pca_connector_ad.types.next_token


class ListConnectorsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_pca_connector_ad.types.max_results.MaxResults"]
    """<p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>"""
    next_token: NotRequired["aws_sdk_pca_connector_ad.types.next_token.NextToken"]
    """<p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectorsRequest:
    out: ListConnectorsRequest = {}  # type: ignore[typeddict-item]
    return out
