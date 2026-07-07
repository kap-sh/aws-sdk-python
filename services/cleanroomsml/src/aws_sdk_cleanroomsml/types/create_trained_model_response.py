"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateTrainedModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.uuid


class CreateTrainedModelResponse(TypedDict, closed=True):
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model.</p>"""
    version_identifier: NotRequired["aws_sdk_cleanroomsml.types.uuid.UUID"]
    r"""<p>The unique version identifier assigned to the newly created trained model. This identifier can be used to reference this specific version of the trained model in subsequent operations such as inference jobs or incremental training.</p> <p>The initial version identifier for the base version of the trained model is \"NULL\".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrainedModelResponse) -> dict:
    out: dict = {}
    out["trainedModelArn"] = value["trained_model_arn"]
    if "version_identifier" in value:
        out["versionIdentifier"] = value["version_identifier"]
    return out


def deserialize_json(data: dict) -> CreateTrainedModelResponse:
    out: CreateTrainedModelResponse = {}  # type: ignore[typeddict-item]
    if "trainedModelArn" in data:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        raise DeserializationError(
            "CreateTrainedModelResponse.trained_model_arn required"
        )
    if "versionIdentifier" in data:
        out["version_identifier"] = data["versionIdentifier"]
    return out
