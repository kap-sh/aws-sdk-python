"""Generated from Smithy shape ``com.amazonaws.connect#ListInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.max_result10
    import capo_connect.types.next_token


class ListInstancesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result10.MaxResult10"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInstancesRequest:
    out: ListInstancesRequest = {}  # type: ignore[typeddict-item]
    return out
