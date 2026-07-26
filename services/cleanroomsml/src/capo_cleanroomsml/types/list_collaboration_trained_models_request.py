"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationTrainedModelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.uuid


class ListCollaborationTrainedModelsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    max_results: NotRequired["capo_cleanroomsml.types.max_results.MaxResults"]
    """<p>The maximum size of the results that is returned per call.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained models you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationTrainedModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationTrainedModelsRequest:
    out: ListCollaborationTrainedModelsRequest = {}  # type: ignore[typeddict-item]
    return out
