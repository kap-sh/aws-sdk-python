"""Generated from Smithy shape ``com.amazonaws.sesv2#ListMultiRegionEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.next_token_v2
    import capo_sesv2.types.page_size_v2


class ListMultiRegionEndpointsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sesv2.types.next_token_v2.NextTokenV2"]
    """<p>A token returned from a previous call to <code>ListMultiRegionEndpoints</code> to indicate the position in the list of multi-region endpoints (global-endpoints).</p>"""
    page_size: NotRequired["capo_sesv2.types.page_size_v2.PageSizeV2"]
    """<p>The number of results to show in a single call to <code>ListMultiRegionEndpoints</code>. If the number of results is larger than the number you specified in this parameter, the response includes a <code>NextToken</code> element that you can use to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultiRegionEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMultiRegionEndpointsRequest:
    out: ListMultiRegionEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
