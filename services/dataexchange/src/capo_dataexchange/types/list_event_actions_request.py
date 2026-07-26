"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListEventActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.max_results


class ListEventActionsRequest(TypedDict, closed=True):
    event_source_id: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The unique identifier for the event source.</p>"""
    max_results: "capo_dataexchange.types.max_results.MaxResults"
    """<p>The maximum number of results returned by a single call.</p>"""
    next_token: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventActionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventActionsRequest:
    out: ListEventActionsRequest = {}  # type: ignore[typeddict-item]
    return out
