"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteTrainedModelOutputRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.uuid


class DeleteTrainedModelOutputRequest(TypedDict):
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model whose output you want to delete.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that is deleting the trained model output.</p>"""
    version_identifier: NotRequired["aws_sdk_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model to delete. If not specified, the operation will delete the base version of the trained model. When specified, only the particular version will be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTrainedModelOutputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTrainedModelOutputRequest:
    out: DeleteTrainedModelOutputRequest = {}  # type: ignore[typeddict-item]
    return out
