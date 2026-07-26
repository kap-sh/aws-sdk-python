"""Generated from Smithy shape ``com.amazonaws.appflow#ListConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.max_results
    import capo_appflow.types.next_token


class ListConnectorsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_appflow.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of items that should be returned in the result set. The default for <code>maxResults</code> is 20 (for all paginated API operations).</p>"""
    next_token: NotRequired["capo_appflow.types.next_token.NextToken"]
    """<p>The pagination token for the next page of data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorsRequest:
    out: ListConnectorsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
