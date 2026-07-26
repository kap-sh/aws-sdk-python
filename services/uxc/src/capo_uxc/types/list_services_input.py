"""Generated from Smithy shape ``com.amazonaws.uxc#ListServicesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_uxc.types.max_results
    import capo_uxc.types.next_token


class ListServicesInput(TypedDict, closed=True):
    next_token: NotRequired["capo_uxc.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results. Use the <code>nextToken</code> value from a previous response.</p>"""
    max_results: NotRequired["capo_uxc.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServicesInput:
    out: ListServicesInput = {}  # type: ignore[typeddict-item]
    return out
