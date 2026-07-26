"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ListManagedResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.max_results


class ListManagedResourcesRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_arc_zonal_shift.types.max_results.MaxResults"]
    """<p>The number of objects that you want to return with this call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedResourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedResourcesRequest:
    out: ListManagedResourcesRequest = {}  # type: ignore[typeddict-item]
    return out
