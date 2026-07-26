"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MLInputChannelsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.ml_input_channel_summary

MLInputChannelsList: TypeAlias = list[
    "capo_cleanroomsml.types.ml_input_channel_summary.MLInputChannelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MLInputChannelsList) -> list:
    import capo_cleanroomsml.types.ml_input_channel_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.ml_input_channel_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MLInputChannelsList:
    import capo_cleanroomsml.types.ml_input_channel_summary

    out: MLInputChannelsList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.ml_input_channel_summary.deserialize_json(item)
        )
    return out
