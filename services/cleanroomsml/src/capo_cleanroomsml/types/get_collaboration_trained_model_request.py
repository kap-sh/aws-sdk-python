"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetCollaborationTrainedModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.uuid


class GetCollaborationTrainedModelRequest(TypedDict, closed=True):
    trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model that you want to return information about.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID that contains the trained model that you want to return information about.</p>"""
    version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model to retrieve. If not specified, the operation returns information about the latest version of the trained model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationTrainedModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollaborationTrainedModelRequest:
    out: GetCollaborationTrainedModelRequest = {}  # type: ignore[typeddict-item]
    return out
