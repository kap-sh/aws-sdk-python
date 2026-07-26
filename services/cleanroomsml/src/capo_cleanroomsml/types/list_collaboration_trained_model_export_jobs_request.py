"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationTrainedModelExportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.uuid


class ListCollaborationTrainedModelExportJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    max_results: NotRequired["capo_cleanroomsml.types.max_results.MaxResults"]
    """<p>The maximum size of the results that is returned per call.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the trained model export jobs that you are interested in.</p>"""
    trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model that was used to create the export jobs that you are interested in.</p>"""
    trained_model_version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model to filter export jobs by. When specified, only export jobs for this specific version of the trained model are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationTrainedModelExportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCollaborationTrainedModelExportJobsRequest:
    out: ListCollaborationTrainedModelExportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
