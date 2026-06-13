"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationMLInputChannelsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.collaboration_ml_input_channel_summary

CollaborationMLInputChannelsList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.collaboration_ml_input_channel_summary.CollaborationMLInputChannelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationMLInputChannelsList) -> list:
    import aws_sdk_cleanroomsml.types.collaboration_ml_input_channel_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.collaboration_ml_input_channel_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationMLInputChannelsList:
    import aws_sdk_cleanroomsml.types.collaboration_ml_input_channel_summary

    out: CollaborationMLInputChannelsList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.collaboration_ml_input_channel_summary.deserialize_json(
                item
            )
        )
    return out
