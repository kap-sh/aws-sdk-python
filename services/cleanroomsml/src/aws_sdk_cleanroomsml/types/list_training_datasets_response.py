"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTrainingDatasetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.training_dataset_list


class ListTrainingDatasetsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    training_datasets: (
        "aws_sdk_cleanroomsml.types.training_dataset_list.TrainingDatasetList"
    )
    """<p>The training datasets that match the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrainingDatasetsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.training_dataset_list

    out["trainingDatasets"] = (
        aws_sdk_cleanroomsml.types.training_dataset_list.serialize_json(
            value["training_datasets"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListTrainingDatasetsResponse:
    out: ListTrainingDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "trainingDatasets" in data:
        import aws_sdk_cleanroomsml.types.training_dataset_list

        out["training_datasets"] = (
            aws_sdk_cleanroomsml.types.training_dataset_list.deserialize_json(
                data["trainingDatasets"]
            )
        )
    else:
        raise DeserializationError(
            "ListTrainingDatasetsResponse.training_datasets required"
        )
    return out
