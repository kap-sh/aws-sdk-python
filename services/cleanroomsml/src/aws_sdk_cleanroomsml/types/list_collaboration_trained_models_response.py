"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationTrainedModelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_list
    import aws_sdk_cleanroomsml.types.next_token


class ListCollaborationTrainedModelsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    collaboration_trained_models: "aws_sdk_cleanroomsml.types.collaboration_trained_model_list.CollaborationTrainedModelList"
    """<p>The trained models in the collaboration that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationTrainedModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_list

    out["collaborationTrainedModels"] = (
        aws_sdk_cleanroomsml.types.collaboration_trained_model_list.serialize_json(
            value["collaboration_trained_models"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationTrainedModelsResponse:
    out: ListCollaborationTrainedModelsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "collaborationTrainedModels" in data:
        import aws_sdk_cleanroomsml.types.collaboration_trained_model_list

        out["collaboration_trained_models"] = (
            aws_sdk_cleanroomsml.types.collaboration_trained_model_list.deserialize_json(
                data["collaborationTrainedModels"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationTrainedModelsResponse.collaboration_trained_models required"
        )
    return out
