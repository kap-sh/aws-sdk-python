"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListRevisionAssetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.id
    import capo_dataexchange.types.max_results


class ListRevisionAssetsRequest(TypedDict, closed=True):
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""
    max_results: "capo_dataexchange.types.max_results.MaxResults"
    """<p>The maximum number of results returned by a single call.</p>"""
    next_token: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRevisionAssetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRevisionAssetsRequest:
    out: ListRevisionAssetsRequest = {}  # type: ignore[typeddict-item]
    return out
