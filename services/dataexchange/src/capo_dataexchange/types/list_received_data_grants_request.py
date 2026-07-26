"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListReceivedDataGrantsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.acceptance_state_filter_values
    import capo_dataexchange.types.max_results


class ListReceivedDataGrantsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_dataexchange.types.max_results.MaxResults"]
    """<p>The maximum number of results to be included in the next page.</p>"""
    next_token: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    acceptance_state: NotRequired[
        "capo_dataexchange.types.acceptance_state_filter_values.AcceptanceStateFilterValues"
    ]
    """<p>The acceptance state of the data grants to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReceivedDataGrantsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReceivedDataGrantsRequest:
    out: ListReceivedDataGrantsRequest = {}  # type: ignore[typeddict-item]
    return out
