"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTrainedModelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.trained_model_list


class ListTrainedModelsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    trained_models: "aws_sdk_cleanroomsml.types.trained_model_list.TrainedModelList"
    """<p>The list of trained models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrainedModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.trained_model_list

    out["trainedModels"] = aws_sdk_cleanroomsml.types.trained_model_list.serialize_json(
        value["trained_models"]
    )
    return out


def deserialize_json(data: dict) -> ListTrainedModelsResponse:
    out: ListTrainedModelsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "trainedModels" in data:
        import aws_sdk_cleanroomsml.types.trained_model_list

        out["trained_models"] = (
            aws_sdk_cleanroomsml.types.trained_model_list.deserialize_json(
                data["trainedModels"]
            )
        )
    else:
        raise DeserializationError("ListTrainedModelsResponse.trained_models required")
    return out
