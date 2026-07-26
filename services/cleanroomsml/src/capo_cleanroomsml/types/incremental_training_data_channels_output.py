"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#IncrementalTrainingDataChannelsOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.incremental_training_data_channel_output

IncrementalTrainingDataChannelsOutput: TypeAlias = list[
    "capo_cleanroomsml.types.incremental_training_data_channel_output.IncrementalTrainingDataChannelOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalTrainingDataChannelsOutput) -> list:
    import capo_cleanroomsml.types.incremental_training_data_channel_output

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.incremental_training_data_channel_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IncrementalTrainingDataChannelsOutput:
    import capo_cleanroomsml.types.incremental_training_data_channel_output

    out: IncrementalTrainingDataChannelsOutput = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.incremental_training_data_channel_output.deserialize_json(
                item
            )
        )
    return out
