"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ModelTrainingDataChannels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.model_training_data_channel

ModelTrainingDataChannels: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.model_training_data_channel.ModelTrainingDataChannel"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelTrainingDataChannels) -> list:
    import aws_sdk_cleanroomsml.types.model_training_data_channel

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.model_training_data_channel.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ModelTrainingDataChannels:
    import aws_sdk_cleanroomsml.types.model_training_data_channel

    out: ModelTrainingDataChannels = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.model_training_data_channel.deserialize_json(
                item
            )
        )
    return out
