"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ModelTrainingDataChannels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.model_training_data_channel

ModelTrainingDataChannels: TypeAlias = list[
    "capo_cleanroomsml.types.model_training_data_channel.ModelTrainingDataChannel"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelTrainingDataChannels) -> list:
    import capo_cleanroomsml.types.model_training_data_channel

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.model_training_data_channel.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ModelTrainingDataChannels:
    import capo_cleanroomsml.types.model_training_data_channel

    out: ModelTrainingDataChannels = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.model_training_data_channel.deserialize_json(item)
        )
    return out
