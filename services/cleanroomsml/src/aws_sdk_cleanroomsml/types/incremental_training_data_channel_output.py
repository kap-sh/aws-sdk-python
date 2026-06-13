"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#IncrementalTrainingDataChannelOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.model_training_data_channel_name
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.uuid


class IncrementalTrainingDataChannelOutput(TypedDict):
    channel_name: "aws_sdk_cleanroomsml.types.model_training_data_channel_name.ModelTrainingDataChannelName"
    """<p>The name of the incremental training data channel that was used.</p>"""
    version_identifier: NotRequired["aws_sdk_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model that was used for incremental training.</p>"""
    model_name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the base trained model that was used for incremental training.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalTrainingDataChannelOutput) -> dict:
    out: dict = {}
    out["channelName"] = value["channel_name"]
    if "version_identifier" in value:
        out["versionIdentifier"] = value["version_identifier"]
    out["modelName"] = value["model_name"]
    return out


def deserialize_json(data: dict) -> IncrementalTrainingDataChannelOutput:
    out: IncrementalTrainingDataChannelOutput = {}  # type: ignore[typeddict-item]
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    else:
        raise DeserializationError(
            "IncrementalTrainingDataChannelOutput.channel_name required"
        )
    if "versionIdentifier" in data:
        out["version_identifier"] = data["versionIdentifier"]
    if "modelName" in data:
        out["model_name"] = data["modelName"]
    else:
        raise DeserializationError(
            "IncrementalTrainingDataChannelOutput.model_name required"
        )
    return out
