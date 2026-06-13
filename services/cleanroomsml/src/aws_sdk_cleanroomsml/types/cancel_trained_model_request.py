"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CancelTrainedModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.uuid


class CancelTrainedModelRequest(TypedDict):
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the trained model job that you want to cancel.</p>"""
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model job that you want to cancel.</p>"""
    version_identifier: NotRequired["aws_sdk_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model to cancel. This parameter allows you to specify which version of the trained model you want to cancel when multiple versions exist.</p> <p>If <code>versionIdentifier</code> is not specified, the base model will be cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelTrainedModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelTrainedModelRequest:
    out: CancelTrainedModelRequest = {}  # type: ignore[typeddict-item]
    return out
