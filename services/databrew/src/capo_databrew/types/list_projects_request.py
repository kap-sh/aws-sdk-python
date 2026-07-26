"""Generated from Smithy shape ``com.amazonaws.databrew#ListProjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.max_results100
    import capo_databrew.types.next_token


class ListProjectsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_databrew.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_databrew.types.max_results100.MaxResults100"]
    """<p>The maximum number of results to return in this request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProjectsRequest:
    out: ListProjectsRequest = {}  # type: ignore[typeddict-item]
    return out
