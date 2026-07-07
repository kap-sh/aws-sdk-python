"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#IncrementalTrainingDataChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.model_training_data_channel_name
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.uuid


class IncrementalTrainingDataChannel(TypedDict, closed=True):
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the base trained model to use for incremental training. This model serves as the starting point for the incremental training process.</p>"""
    version_identifier: NotRequired["aws_sdk_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the base trained model to use for incremental training. If not specified, the latest version of the trained model is used.</p>"""
    channel_name: "aws_sdk_cleanroomsml.types.model_training_data_channel_name.ModelTrainingDataChannelName"
    """<p>The name of the incremental training data channel. This name is used to identify the channel during the training process and must be unique within the training job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalTrainingDataChannel) -> dict:
    out: dict = {}
    out["trainedModelArn"] = value["trained_model_arn"]
    if "version_identifier" in value:
        out["versionIdentifier"] = value["version_identifier"]
    out["channelName"] = value["channel_name"]
    return out


def deserialize_json(data: dict) -> IncrementalTrainingDataChannel:
    out: IncrementalTrainingDataChannel = {}  # type: ignore[typeddict-item]
    if "trainedModelArn" in data:
        out["trained_model_arn"] = data["trainedModelArn"]
    else:
        raise DeserializationError(
            "IncrementalTrainingDataChannel.trained_model_arn required"
        )
    if "versionIdentifier" in data:
        out["version_identifier"] = data["versionIdentifier"]
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    else:
        raise DeserializationError(
            "IncrementalTrainingDataChannel.channel_name required"
        )
    return out
