"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetTrainedModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.uuid


class GetTrainedModelRequest(TypedDict, closed=True):
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model that you are interested in.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that created the trained model that you are interested in.</p>"""
    version_identifier: NotRequired["aws_sdk_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model to retrieve. If not specified, the operation returns information about the latest version of the trained model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrainedModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTrainedModelRequest:
    out: GetTrainedModelRequest = {}  # type: ignore[typeddict-item]
    return out
