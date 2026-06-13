"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#IncrementalTrainingDataChannels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.incremental_training_data_channel

IncrementalTrainingDataChannels: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.incremental_training_data_channel.IncrementalTrainingDataChannel"
]


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalTrainingDataChannels) -> list:
    import aws_sdk_cleanroomsml.types.incremental_training_data_channel

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.incremental_training_data_channel.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IncrementalTrainingDataChannels:
    import aws_sdk_cleanroomsml.types.incremental_training_data_channel

    out: IncrementalTrainingDataChannels = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.incremental_training_data_channel.deserialize_json(
                item
            )
        )
    return out
