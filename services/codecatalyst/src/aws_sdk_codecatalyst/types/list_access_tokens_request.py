"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListAccessTokensRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListAccessTokensRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessTokensRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessTokensRequest:
    out: ListAccessTokensRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
