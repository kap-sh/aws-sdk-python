"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListDataSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.max_results


class ListDataSetsRequest(TypedDict, closed=True):
    max_results: "capo_dataexchange.types.max_results.MaxResults"
    """<p>The maximum number of results returned by a single call.</p>"""
    next_token: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    origin: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataSetsRequest:
    out: ListDataSetsRequest = {}  # type: ignore[typeddict-item]
    return out
