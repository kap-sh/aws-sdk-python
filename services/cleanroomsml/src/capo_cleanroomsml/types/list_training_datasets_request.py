"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTrainingDatasetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.next_token


class ListTrainingDatasetsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    max_results: NotRequired["capo_cleanroomsml.types.max_results.MaxResults"]
    """<p>The maximum size of the results that is returned per call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrainingDatasetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTrainingDatasetsRequest:
    out: ListTrainingDatasetsRequest = {}  # type: ignore[typeddict-item]
    return out
