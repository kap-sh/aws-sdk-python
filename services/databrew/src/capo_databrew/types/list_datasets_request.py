"""Generated from Smithy shape ``com.amazonaws.databrew#ListDatasetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.max_results100
    import capo_databrew.types.next_token


class ListDatasetsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_databrew.types.max_results100.MaxResults100"]
    """<p>The maximum number of results to return in this request. </p>"""
    next_token: NotRequired["capo_databrew.types.next_token.NextToken"]
    """<p>The token returned by a previous call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetsRequest:
    out: ListDatasetsRequest = {}  # type: ignore[typeddict-item]
    return out
