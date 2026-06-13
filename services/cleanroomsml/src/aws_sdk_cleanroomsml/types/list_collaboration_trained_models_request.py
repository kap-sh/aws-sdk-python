"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationTrainedModelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.uuid


class ListCollaborationTrainedModelsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_cleanroomsml.types.max_results.MaxResults"]
    """<p>The maximum size of the results that is returned per call.</p>"""
    collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained models you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationTrainedModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationTrainedModelsRequest:
    out: ListCollaborationTrainedModelsRequest = {}  # type: ignore[typeddict-item]
    return out
